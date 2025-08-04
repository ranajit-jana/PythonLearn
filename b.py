#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 08:55:05 2025

@author: rj
"""

class Student:
    
    def __init__(self, percentage):
        self.percentage = percentage
        
    def showpercentage(self):
        print(" percentage is ", self.percentage)
        
    def showgrade(self):
        if(self.percentage > 85):
            print("Distinction")
        elif(self.percentage >= 70):
            print("First Class")
        elif(self.percentage >=60):
            print("Third Class")
        elif(self.percentage >=50):
            print("Pass")
        
        
        
s = Student(90)
s.showgrade()

nextstudent = Student(66)
nextstudent.showgrade()