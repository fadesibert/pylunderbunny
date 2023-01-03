# pylunderbunny
Cycling Integration App

# Architecture
ESP32 (micropython v1.19.1)

# Setup
## Clone repo
git clone https://github.com/fadesibert/pylunderbunny

## Install Terminal App
### Mac
```brew install picocom```
### Linux
```sudo apt-get install picocom```
(optional) - add the user to the dialout group so that sudo isn't required to access the TTY

```sudo usermod -G dialout fadesibert```
#### Install Uploader (for convenience, rather than copy/paste
pip install adafruit-ampy

## Setup clean ESP32
_Best to use an ESP32 Devkit, preferably with USB connector for easy upload / prototyping_

### Flash with Micropython firmware
[http://docs.micropython.org/en/latest/esp32/quickref.html#installing-micropython](micropython docs)
* Download the correct firmware for your ESP32 (can also build your own, but not necessary): https://micropython.org/download/esp32/
* Install esptool (any name for a venv will do - I chose mp-host - mp for micropython, host because this is the "utility" side, rather than micropython running locally)
** python3 -mvenv mp-host
** source mp-host/bin/activate
** pip install esptool
** _ here, you need to hold the "BOOT" button, run the command and then release it - this boots the ESP32 into "download" mode rather than "run" mode_
** esptool.py --port /dev/ttyUSB0 erase_flash
** esptool.py --port /dev/ttyUSB0 --chip esp32 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin

### Connect to Python interpreter on USB dev port
`picocom -b 115200 /dev/ttyUSB0`

replace with name of autodetected USB TTY - could be /dev/ttySXXX or /dev/ttyUSBxx, and -b specifies baud rate - usually 115200 - but can be any of the standard ones (9600, 57600, 115200)

## New Branch
* ```git checkout -b branch-name-username```
* ```...```
* ```git commit -a -S -m "a useful commit message"```
* ```git push origin HEAD```

## Upload code to Microcontroller
For convenience (and by default on ESP32) call your file main.py. This is, IIRC, configurable
```ampy --port /dev/ttyUSB0 put main.py```

* Reset the microcontroller to restart the program.
* Standard Out (ouput of `print("foo")` is written to the terminal port)

________
```
fadesibert@pop-os:~/pylunderbunny$ sudo picocom -b 115200 /dev/ttyUSB0
picocom v3.1

port is        : /dev/ttyUSB0
flowcontrol    : none
baudrate is    : 115200
parity is      : none
databits are   : 8
stopbits are   : 1
escape is      : C-a
local echo is  : no
noinit is      : no
noreset is     : no
hangup is      : no
nolock is      : no
send_cmd is    : sz -vv
receive_cmd is : rz -vv -E
imap is        :
omap is        :
emap is        : crcrlf,delbs,
logfile is     : none
initstring     : none
exit_after is  : not set
exit is        : no

rst:0x1 (POWERON_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:2
load:0x3fff0030,len:4540
ho 0 tail 12 room 4
load:0x40078000,len:12344
ho 0 tail 12 room 4
load:0x40080400,len:4124
entry 0x40080680
MicroPython v1.19.1 on 2022-06-18; ESP32 module with ESP32
Type "help()" for more information.
>>>

```
