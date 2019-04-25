## Jupyter on Pi
* [Example](https://www.hackster.io/mjrobot/rpi-physical-computing-using-jupyter-notebook-056fa8)
```
sudo apt-get update
sudo apt-get install python3-matplotlib
sudo apt-get install python3-scipy
sudo pip3 install --upgrade pip
reboot
sudo pip3 install jupyter
sudo pip3 install jupyterlab
```

* [Connect from remote machine via SSH](https://www.blopig.com/blog/2018/03/running-jupyter-notebook-on-a-remote-server-via-ssh/) -> first run  `jupyter notebook --generate-config` then set default password using `jupyter notebook password`. Can then run notebook or lab (`jupyter lab --port=9000 --no-browser &`) and connect with ssh: `ssh -N -f -L 9000:localhost:9000 pi@ip` and visit `http://localhost:9000`

## Mosquitto MQTT
* https://hub.docker.com/_/eclipse-mosquitto (docker, bit problematic)
* https://theembeddedlab.com/tutorials/install-mosquitto-on-a-raspberry-pi/ (direct install)

## Samba
* https://www.juanmtech.com/samba-file-sharing-raspberry-pi/

## SCP
* https://www.raspberrypi.org/documentation/remote-access/ssh/scp.md

## VSCode
* Use Remote extension to edit files on the Pi from VScode on another machine -> https://github.com/rafaelmaiolla/remote-vscode (some more guidance [here](https://www.hackster.io/Ladvien/editing-raspberry-pi-code-remotely-from-visual-studio-code-9d42e0))