#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 08:22:01 2025

@author: rj
"""
import traceback

class Divide:
    
    def __init__(self, divisor, divident):
        self.divisor  = divisor
        self.divident = divident
        
    def performDivisionOperation(self):
        try:
            if(self.divident == 0):
                raise ZeroDivisionError(" The divident cannot be zero")
            result = self.divisor/self.divident
            x = 10
        except Exception:
            traceback.print_exc()
        return x
    

d = Divide(10, 2)
rs = d.performDivisionOperation()
print(" returned value :" , rs)
        