# simple_mjpeg_streamer_http_server
simple python mjpeg streamer http server -> https://github.com/n3wtron/simple_mjpeg_streamer_http_server/tree/python3

* It can only handle one connection at a time
* Hitting Ctrl-C to kill the program doesn't allow you to cleanly exit the program ... try/expect don't seem to work for this and it is because of how BaseTTPServer is designed.

# home assistant
View stream with the following:
```
stream:
camera:
  - platform: mjpeg
    mjpeg_url: http://127.0.0.1:8080/cam.mjpg 
```