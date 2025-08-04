# -*- coding: utf-8 -*-


from com.corp.company import Company

class Employee:
    
    def __init__(self):
        c = Company()
        c.set_secret("soe")
        secret = c.get_secret()
        
        print(" secret:", secret)
        print("Company: ", c.companyName ,"  - location :", c.location)
        

        
        
e = Employee()
#print( "employee is up)
