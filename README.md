# panel_com3
## python3 compatible version of VR control functions originally developed by Seth Budick and functionalized into python by Will Dickson and is found here: https://github.com/iorodeo/panel_comm

### installation:
Navigate to a place to clone the repository 
```
cd ~/Desktop
```

then git clone:
```
git clone https://github.com/dstupski/panel_com3.git
```

go inside your clone repository and pip3 install:

```
pip3 install .
```
### runnning the example:
The Reiser panel controller operates by inserting an SD card preloaded with pattern files (see https://reiserlab.github.io/Modular-LED-Display/G3/)

This example loads a pattern and rotates it across the arena.  Assumes pattern has at least 48 "x frames" 

TODO: PATTERN REPO FOR TESTING

panel_com
=============

panel_comm provides a serial port interface to Michael Reiser's Panel controller
 


Installation

   * Installation instructions can be found in the INSTALL file.  

Examples

   * Examples demonstrating how to use panel_comm can be found in 
     the panel_comm/examples directory. 
     
Author

   * Will Dickson (wbd@caltech.edu) - adapted from the Panel_com class
     of Seth budick in PControl. 
