## TensorFlow Lite for Microcontrollers
* https://www.tensorflow.org/lite/microcontrollers/overview
* TensorFlow Lite for Microcontrollers is an experimental port of TensorFlow Lite aimed at microcontrollers and other devices with only kilobytes of memory.

## Arduino
* https://blog.arduino.cc/2019/10/15/get-started-with-machine-learning-on-arduino/
* https://github.com/arduino/ArduinoTensorFlowLiteTutorials

#### `micro_speech` 
* `micro_speech` -> One of the first steps with an Arduino board is getting the LED to flash. Here, we’ll do it with a twist by using TensorFlow Lite Micro to recognise voice keywords. It has a simple vocabulary of “yes” and “no.” Remember this model is running locally on a microcontroller with only 256KB of RAM, so don’t expect commercial ‘voice assistant’ level accuracy – it has no Internet connection and on the order of 2000x less local RAM available.
* Works OK, bias towards it recognising `Yes` over `No`