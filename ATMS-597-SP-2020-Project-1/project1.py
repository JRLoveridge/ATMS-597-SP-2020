# -*- coding: utf-8 -*-
"""Project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/JRLoveridge/ATMS-597-SP-2020/blob/cathy-edits/ATMS-597-SP-2020-Project-1/Project1.ipynb
"""

import numpy as np

class TemperatureConverter(object):
    """
    A temperature converter that converts temperatures interchangeably between degrees Celsius, Fahrenheit, and Kelvin.
    Works with lists or numpy arrays as input, and returns the same numerical type.
    """
    def __init__(self, temperature, units='Kelvin'):
        """
        TODO
        """
        assert units in ['Fahrenheit', 'Celsius', 'Kelvin'], 'Units must be valid.'
        self._temperature = np.atleast_1d(temperature) #internally store numpy array.
        self._units = units
        if type(temperature) == int:
            temperature = float(temperature)
        self._input_type = type(temperature) #preserve old input type/dtype

    @staticmethod
    def convert_temperature(temperature, in_units='Kelvin', out_units='Kelvin'):
      """
      Option to write the whole thing without storing any information in the object.
      """

    def set_temperature(self, temperature, units='Kelvin'):
        """
        TODO
        """
        assert units in ['Fahrenheit', 'Celsius', 'Kelvin'], 'Units must be valid.'
        self._temperature = np.atleast_1d(temperature)
        self._units = units
        if type(temperature) == int:
            temperature = float(temperature)
        self._input_type = type(temperature) #preserve old input type/dtype

    def get_temperature(self, units='Kelvin'):
        """
        TODO
        """
        assert units in ['Fahrenheit', 'Celsius', 'Kelvin'], 'Units must be valid.'     

        if units == 'Fahrenheit':
          converted_temp =  self.to_fahrenheit()
        elif units == 'Celsius':
          converted_temp =  self.to_celsius()
        elif units == 'Kelvin':
          converted_temp =  self.to_kelvin()

        if self._input_type != type(converted_temp):
          final_output = self._input_type(converted_temp)
        else:
          final_output = converted_temp

        return final_output

    def to_kelvin(self):
        """
        Converts a temperature of any unit to Kelvin.
        """
        if self._units == 'Fahrenheit':
            returned_temperature = (self._temperature + 459.67)*(5/9)
        elif self._units == 'Celsius':
            returned_temperature = self._temperature + 273.15
        else:
            returned_temperature = self._temperature


        return returned_temperature
  
    def to_celsius(self):
        """
        Converts a temperature of any unit to Celsius.
        """

        if self._units == 'Fahrenheit':
            returned_temperature = (self._temperature - 32) * (5/9)
        elif self._units == 'Kelvin':
            returned_temperature = self._temperature - 273.15
        else:
            returned_temperature = self._temperature

        return returned_temperature

    def to_fahrenheit(self):
        """
        Converts a temperature of any unit to Fahrenheit.
        """

        if self._units == 'Celsius':
            returned_temperature = self._temperature*(9/5) + 32
        elif self._units == 'Kelvin':
            returned_temperature = self._temperature*(9/5) - 459.67
        else:    
            returned_temperature = self._temperature

        return returned_temperature

temp_conv = TemperatureConverter([50,60.0,12830.0],units='Celsius')



b
