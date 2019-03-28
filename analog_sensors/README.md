# Analog Sensors
In this lab, we utilize an MCP3002 Analog to Digital Converter (ADC) to read from a TMP36 temperature sensor as well as a photoresistor (Light Dependent Resistor - LDR).  Utilizing the readings from these two analog sensors, we will trigger a red LED when the temperature gets too hot and a white LED when it gets too dark.

We will also utilize a new python library we haven't used previously.  The *gpiozero* library was included with the standard Raspian install and greatly simplifies working with electrical components.  Interacting with the MCP3002 is super simple with *gpiozero*.

## MCP3002
This ADC has two channels enabling it to read up to two sensors.  This is a cheaper alternative to the MCP3008 which has eight channels.  Both of these chips utilize a Serial Peripheral Interface (SPI) which is a master/slave architecture where our Raspberry Pi will serve as the master querying the slave for sensor values.  The sensors are plugged into either channel 0 (pin 2) or channel 1 (pin 3).  The ADC reads the voltages on those pins, converts them to a floating point value, and returns the results to the master.

## TMP36
This sensor has three pins and will vary the voltage on the center pin in relation to the temperature of the chip.  In this lab, we will pinch the top of the TMP36 to raise the temperature.  As the temperature increases, so does the voltage on the center pin.  The formula's that I have found output in Celsius but could be later converted to Fahrenheit.

```
Temp in °C = [(Vout in mV) - 500] / 10
Temp in °C = [(Vout V) - .5] / 100
```

## Photoresistor (LDR)
This inexpensive device varies it's resistance based on the amount of light it receives.  As the light decreases, the resistance increases.  Resistance can vary widely from a few hundred Ohms in bright sunlight up to 200k Ohms in the dark.  By pairing up the LDR with a 10k resistor in a voltage divider circuit, as the resistance of the LDR increases, the voltage drop across it does as well.  It is this voltage change that we'll send to the MCP3002.

## Required Hardware
1. Raspberry Pi 3
2. MCP3002
3. TMP36
4. Photoresistor (LDR)
5. White LED (too dark)
6. RED LED (too hot)
7. 10k Resistor
8. 2 x 220 Ohm resistors

## Topics to Discuss
1. Analog
2. Digital
3. Analog to Digital Conversion
3. Voltage Divider Circuit
4. Single-Threading vs Multi-Threading
