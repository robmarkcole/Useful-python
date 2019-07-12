#!/usr/bin/python3
"""
    Author: Igor Maculan - n3wtron@gmail.com
    A Simple mjpg stream http server
"""
import signal
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

import cv2
from PIL import Image

capture = None
to_exit = False

class CamHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('.mjpg'):
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=jpgboundary')
            self.end_headers()
            global to_exit
            while not to_exit:
                rc, img = capture.read()
                if not rc:
                    continue
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                jpg = Image.fromarray(imgRGB)
                jpg_bytes = jpg.tobytes()
                self.wfile.write(str.encode("\r\n--jpgboundary\r\n"))
                self.send_header('Content-type', 'image/jpeg')
                self.send_header('Content-length', len(jpg_bytes))
                self.end_headers()
                jpg.save(self.wfile, 'JPEG')
                time.sleep(0.05)
            return
        if self.path.endswith('.html'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(str.encode('<html><head></head><body>'))
            self.wfile.write(str.encode('<img src="http://127.0.0.1:8080/cam.mjpg"/>'))
            self.wfile.write(str.encode('</body></html>'))
            return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


def quit(sig,frame):
    print("Exiting...")
    global to_exit
    global capture
    global server
    to_exit = True
    capture.release()
    server.socket.close()
    exit(0)


def main():
    signal.signal(signal.SIGINT, quit)
    global capture
    global server
    global img
    capture = cv2.VideoCapture(0)
    ip = '0.0.0.0'
    port = 8080
    server = ThreadedHTTPServer((ip, port), CamHandler)
    print("server started at " + ip + ':' + str(port))
    print('find video at http://127.0.0.1:8080/cam.mjpg')
    server.serve_forever()


if __name__ == '__main__':
    main()
