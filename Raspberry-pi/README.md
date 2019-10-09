# Radpberry pi
* To have a headless pi start with ssh enabled just put an empty file named `ssh` (no file extension) on `boot` SD card image
* To configure wifi add a `wpa_supplicant.conf` file on `boot` SD card image

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

## Python
* [Build python 3.6.5](https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f) (commands below) -> does not update the PATH python automatically but tested on 8/6/2019 successfully

```
$ wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
$ tar xf Python-3.6.5.tar.xz
$ cd Python-3.6.5
$ ./configure
$ make
$ sudo make altinstall
```

Then:
```
pi@raspberrypi:~/Downloads/Python-3.6.5 $ ./python
Python 3.6.5 (default, Jun  8 2019, 07:25:32)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
 
## Mosquitto MQTT
* `sudo apt-get install mosquitto mosquitto-clients` -> runs automatically
* https://hub.docker.com/_/eclipse-mosquitto (docker, simple and easy)

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
* [Picamera mjpeg stream](https://picamera.readthedocs.io/en/release-1.13/recipes2.html#web-streaming)
* [https://kerberos.io/](https://kerberos.io/) is very full featured, exposes camera as mjpeg, save images to S3, fire MQTT message on captures
* [Motion](https://motion-project.github.io/motion_config.html) has been around for years and works well, be sure to edit the config file e.g. to allow viewing on remote machines. Motion detection algorithm might be better than kerberos
* https://github.com/rob5standingby/raspberry-pi-s3-cam
* [Docker container for streaming a Raspberry Pi's camera via HTTP/MJPG](https://github.com/pschmitt/docker-picamera)
* [Simple take picture flask app](https://github.com/stlehmann/picamera/blob/master/flaskapp/app.py)

## Gstreamer
* `sudo apt-get install gstreamer-tools` or if [specific version required](https://github.com/pimoroni/mlx90640-library/blob/master/examples/src/rawrgb.cpp) `sudo apt-get install gstreamer1.0-tools`

## Find a file
* https://www.bitpi.co/2015/02/15/using-find-command-raspbian/

## View images on pi on Mac via SSH
* https://github.com/eddieantonio/imgcat

## MariaDB
* https://howtoraspberrypi.com/mariadb-raspbian-raspberry-pi/

## Pip3
* https://www.raspberrypi.org/documentation/linux/software/python.md
* `sudo apt-get install python3-pip`

## PiCamera
* https://picamera.readthedocs.io/en/release-1.13/index.html
* `sudo apt-get install python3-picamera`

## OpenCV
* `sudo apt install python3-opencv` to [install from the Raspbian official package manager](https://raspberrypi.stackexchange.com/questions/100253/how-can-i-install-opencv-on-raspberry-pi-4-raspbian-buster)

## Pillow
* Very useful library for working with images
* [Install](https://www.techcoil.com/blog/how-to-setup-python-imaging-library-pillow-on-raspbian-stretch-lite-for-processing-images-on-your-raspberry-pi/)

```
sudo apt-get update
sudo apt-get install libjpeg-dev -y
sudo apt-get install zlib1g-dev -y
sudo apt-get install libfreetype6-dev -y
sudo apt-get install liblcms1-dev -y
sudo apt-get install libopenjp2-7 -y
sudo apt-get install libtiff5 -y
pip3 install pillow
```

## Minio
* Local S3
* Not officially supported on pi but as it is just a Go package, can be installed. [Instructions here](https://github.com/christianbaun/ossperf/wiki/Minio-on-a-Raspberry-Pi-3-with-Raspbian-(Debian-Jessie-8.0))

```
$ wget https://dl.minio.io/server/minio/release/linux-arm/minio
$ chmod +x minio 
$ ./minio server --address ":8080"  s3-storage-folder 
```