# README #

This is GUI app for controlling GNSS Tevogs Tesbench. This app allows to control testbench and start spin it to test the GNSS device. It also allows you to simply download the log file to your computer via sftp. 

Parameters for app are set in Rounds per second of motor, for example 20 rps will result in about 40km/h of angular speed at the end of testbench, where reciever devices are placed.
Second parameter is timelength of spin, whic is set in seconds. 

WARNING testbench will turn into starting position to where is inductive sensor placed at startup and before every spinsession start, dont stand in the way of arms of testbench. Use emergency stop to get out of way. Then release the emergency stop WARNING


### What is this repository for? ###

* Quick summary
* Set up
* Usage

### Prerequisities ###
* python3 is required
* Create virtual enviroment in folder with project
* Activate it by . "venv/bin/acitvate"
* Required packages are written in requirements.txt
* Run "pip install -r requirements.txt" in folder with project

### Start GUI ###
* After installing requirements it is possible to run app
* Run "python3 main.py"

### Usage ###
* Power up testbench
* Connect to testbench via wifi 
* Start GUI app, whic automatically connects to port, it may sometimes take a while for port to be able to connect
* Spin testbench
