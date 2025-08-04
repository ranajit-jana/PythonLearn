#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 09:11:49 2025

@author: rj
"""


def test():
    try:
        x = 10
        with open("C:/some.txt","w") as file:
            file.write("SOme string")
            print( " file operation successful")



    except FileNotFoundError:
        print("Exeptiuon in file execution")
    except PermissionError:
        print(" Permission error")    
    except Exception:
        print(" unexpected exception")
    finally:
        print(x)
        
        
test()