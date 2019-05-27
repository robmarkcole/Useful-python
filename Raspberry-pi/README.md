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
* https://hub.docker.com/_/eclipse-mosquitto (docker, simple and easy)
* https://theembeddedlab.com/tutorials/install-mosquitto-on-a-raspberry-pi/ (direct install)

## Samba
* Expose folders as a shared drive
* https://www.juanmtech.com/samba-file-sharing-raspberry-pi/

## SFTP
* SFTP: Securely and interactively transfer files over SSH -> use Filezilla for a nice UI
* https://www.raspberrypi.org/documentation/remote-access/ssh/sftp.md

## SCP
* Copy file over the network using SSH, not interactive
* https://www.raspberrypi.org/documentation/remote-access/ssh/scp.md
* Compare SCP & SFTP -> https://www.maketecheasier.com/scp-vs-sftp/

## Run scrips on rpi startup
* Have a script run on pi startup -> [rc.local](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md)

## VSCode
* Use Remote extension to edit files on the Pi from VScode on another machine -> https://github.com/rafaelmaiolla/remote-vscode (some more guidance [here](https://www.hackster.io/Ladvien/editing-raspberry-pi-code-remotely-from-visual-studio-code-9d42e0))

## Streaming from cameras
* [https://kerberos.io/](https://kerberos.io/) is very full featured, exposes camera as mjpeg, save images to S3, fire MQTT message on captures
* [Motion](https://motion-project.github.io/motion_config.html) has been around for years and works well, be sure to edit the config file e.g. to allow viewing on remote machines. Motion detection algorithm might be better than kerberos
* https://github.com/rob5standingby/raspberry-pi-s3-cam

## Find a file
* https://www.bitpi.co/2015/02/15/using-find-command-raspbian/

## Minio
* Local S3
* Not officially supported on pi but as it is just a Go package, can be installed. [Instructions here](https://github.com/christianbaun/ossperf/wiki/Minio-on-a-Raspberry-Pi-3-with-Raspbian-(Debian-Jessie-8.0))

```
$ wget https://dl.minio.io/server/minio/release/linux-arm/minio
$ chmod +x minio 
$ ./minio server --address ":8080"  s3-storage-folder 
```