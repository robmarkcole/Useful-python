# The following script is an adjusted version of Aaron Bell's script
# http://www.aaronbell.com/how-to-hack-amazons-wifi-button/

# improvement from original script:
# - New dash buttons can be added by just adding a new nickname to the macs dictionary
# - Will not trigger multiple events for one press (see trigger_timeout below)

# if you want to run this script as an ubuntu service, check out
# http://askubuntu.com/questions/175751/how-do-i-run-a-python-script-in-the-background-and-restart-it-after-a-crash

import socket
import struct
import binascii
import time
import json
import urllib2
import datetime

# Use your own IFTTT key, not this fake one
ifttt_key = 'fakekey'
# the number of seconds after a dash button is pressed that it will not trigger another event
# the reason is that dash buttons may try to send ARP onto the network during several seconds
# before giving up
trigger_timeout = 5

# Replace these fake MAC addresses and nicknames with your own
# the nickname of the dash buttons is what will be used as the event name
# when triggering the IFTTT maker channel, e.g. https://maker.ifttt.com/trigger/<nickname>/with/key/<ifttt_key>
macs = {
    '747500000001' : 'dash_gerber',
    '747500000002' : 'dash_elements1',
    '747500000003' : 'dash_elements2',
    '747500000004' : 'dash_cottonelle',
    '747500000005' : 'dash_huggies'
}

# for recording the last time the event was triggered to avoid multiple events fired
# for one press on the dash button
trigger_time = {}

# Trigger a IFTTT URL where the event is the same as the strings in macs (e.g. dash_gerber)
# Body includes JSON with timestamp values.
def trigger_url_generic(trigger):
    data = '{ "value1" : "' + time.strftime("%Y-%m-%d") + '", "value2" : "' + time.strftime("%H:%M") + '" }'
    req = urllib2.Request( 'https://maker.ifttt.com/trigger/'+trigger+'/with/key/'+ifttt_key , data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    response = f.read()
    f.close()
    return response

def record_trigger(trigger):
    print 'triggering '+ trigger +' event, response: ' + trigger_url_generic(trigger)

def is_within_secs(last_time, diff):
    return (datetime.datetime.now() - last_time).total_seconds() < (diff +1)

# check if event has triggered within the timeout already
def has_already_triggered(trigger):
    global trigger_time
    
    if trigger in trigger_time:
        if (is_within_secs(trigger_time[trigger], trigger_timeout)):
            return True

    trigger_time[trigger] = datetime.datetime.now()
    return False



rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))

while True:
    packet = rawSocket.recvfrom(2048)
    ethernet_header = packet[0][0:14]
    ethernet_detailed = struct.unpack("!6s6s2s", ethernet_header)
    # skip non-ARP packets
    ethertype = ethernet_detailed[2]
    if ethertype != '\x08\x06':
        continue
    arp_header = packet[0][14:42]
    arp_detailed = struct.unpack("2s2s1s1s2s6s4s6s4s", arp_header)
    source_mac = binascii.hexlify(arp_detailed[5])
    source_ip = socket.inet_ntoa(arp_detailed[6])
    dest_ip = socket.inet_ntoa(arp_detailed[8])
    if source_mac in macs:
        
        if has_already_triggered(macs[source_mac]):
            print "Culled duplicate trigger " + macs[source_mac]
        else:
            record_trigger(macs[source_mac])

    elif source_ip == '0.0.0.0':
        print "Unknown dash button detected with MAC " + source_mac
