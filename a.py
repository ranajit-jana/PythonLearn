#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 08:32:33 2025

@author: rj
"""

class Vehicle:
    def __init__(self):
        self.__speed = 10
    def __checkspeed(self):
        print( "vehicle is moving at :" , self.__speed )
        
        
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        #self.__speed = 150
    def checkspeed(self):
        v = Vehicle()
        print("Car Speed is ", v._Vehicle__speed)
        
        
c = Car()
c.checkspeed()
print(c._Vehicle__speed)
        
        