# Push-Button-LED-Toggle-using-raspberry-pi-pico-w
This project demonstrates how to use a push button to toggle the state of an LED on the Raspberry Pi Pico W. Each press of the button changes the LED state from ON to OFF or from OFF to ON.

## Components Used

* Raspberry Pi Pico W
* LED
* Push Button
* Breadboard
* Jumper Wires

## Programming Language

* MicroPython

## Features

* Push button input detection
* LED toggle functionality
* State tracking
* Internal pull-up resistor configuration
* Real-time monitoring

## Project Code

[Click here to check out the code](code/button_toggle_switch_for_led_control_on_raspberry_pico_w.py)

## Project Images

[Click here to check out the project images](images/toggle_1.jpg)

## Project Demo video

[Click here to check out the demo video](https://youtu.be/N022qx1EfGI?si=Ct4VayDLo9Uz3r3V)

## Pin Connections

* Push Button → GP14
* LED → GP15

## How It Works

The program continuously monitors the push button state. When a button press is detected, the LED state is toggled. If the LED is OFF, it turns ON. If the LED is ON, it turns OFF. The process repeats every time the button is pressed.

## Author

Moses Olorunfemi Kolawole
