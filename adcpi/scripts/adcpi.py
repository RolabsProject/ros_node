#!/usr/bin/env python
# read abelectronics ADC Pi V2 board inputs with repeating reading from each channel.
# 12 bit data rate
# # Requries Python 2.7
# Requires SMself.bus 
# I2C API depends on I2C support in the kernel

# Version 1.0  - 18/01/2014
# Version History:
# 1.0 - Initial Release

#
# Usage: changechannel(address, hexvalue) to change to new channel on adc chips
# Usage: getself.adcreading(address, hexvalue) to return value in volts from selected channel.
#
# address = self.adc_address1 or self.adc_address2 - Hex address of I2C chips as configured by board header pins.

from smbus import SMBus
import re


class adcpi:

	def __init__(self):
		self.adc_address1 = 0x68
		self.adc_address2 = 0x69

		# create byte array and fill with initial values to define size
		self.adcreading = bytearray()

		self.adcreading.append(0x00)
		self.adcreading.append(0x00)
		self.adcreading.append(0x00)
		self.adcreading.append(0x00)

		varDivisior = 1 # from pdf sheet on adc addresses and config
		self.varMultiplier = (2.4705882/varDivisior)/1000

		# detect i2C port number and assign to i2c_self.bus
		for line in open('/proc/cpuinfo').readlines():
		    m = re.match('(.*?)\s*:\s*(.*)', line)
		    if m:
			(name, value) = (m.group(1), m.group(2))
			if name == "Revision":
			    if value [-4:] in ('0002', '0003'):
				i2c_bus = 0
			    else:
				i2c_bus = 1
			    break
			       

		self.bus = SMBus(i2c_bus)
	 
	def changechannel(self, address, adcConfig):
		tmp= self.bus.write_byte(address, adcConfig)

	def getadcreading(self, address, adcConfig):
		self.adcreading = self.bus.read_i2c_block_data(address,adcConfig)
		h = self.adcreading[0]
		l = self.adcreading[1]
		s = self.adcreading[2]
	
		# wait for new data
		while (s & 128):
			self.adcreading = self.bus.read_i2c_block_data(address,adcConfig)
			h = self.adcreading[0]
			l = self.adcreading[1]
			s = self.adcreading[2]
		
	
		# shift bits to product result
		t = (h << 8) | l
		# check if positive or negative number and invert if needed
		if (h > 128):
			t = ~(0x020000 - t)
		return t * self.varMultiplier
	
	def capteurRead(self, iCapteur):
		adcConfigTab = [ 0x90, 0xB0, 0xD0, 0xF0, 0x90, 0xB0, 0xD0, 0xF0]
		adcConfigVal = adcConfigTab[iCapteur]
		adc_address  = self.adc_address1
		if (iCapteur >= 4):
			adc_address  = self.adc_address2
			
		self.changechannel(adc_address, adcConfigVal)
		return self.getadcreading(adc_address,adcConfigVal)

