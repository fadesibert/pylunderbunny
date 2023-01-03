# pylunderbunny
Cycling Integration App

# Architecture
ESP32 (micropython v1.19.1)

# Setup
## Clone repo
git clone https://github.com/fadesibert/pylunderbunny

## Install Terminal App
### Mac
homebrew install picocom
### Linux
sudo apt-get install picocom
#### Install Uploader (for convenience, rather than copy/paste
sudo apt-get install ampy

## Setup clean ESP32
_Best to use an ESP32 Devkit, preferably with USB connector for easy upload / prototyping_

### Flash with Micropython firmware
[http://docs.micropython.org/en/latest/esp32/quickref.html#installing-micropython](micropython docs)
### Connect to Python interpreter on USB dev port
`picocom -b 115200 /dev/ttyUSB0`

replace with name of autodetected USB TTY - could be /dev/ttySXXX or /dev/ttyUSBxx, and -b specifies baud rate - usually 115200 - but can be any of the standard ones (9600, 57600, 115200)

## New Branch
`git checkout -b branch-name-username`
`...`
`git commit -a -S -m "a useful commit message"`
`git push origin HEAD`

## Upload code to Microcontroller
For convenience (and by default on ESP32) call your file main.py. This is, IIRC, configurable
`ampy --port /dev/ttyUSB0 put main.py`

* Reset the microcontroller to restart the program.
* Standard Out (ouput of `print("foo")` is written to the terminal port)

