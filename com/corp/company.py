# -*- coding: utf-8 -*-


class Company:
    
    companyName = "DSL"
    def __init__(self):
        self.location = "Bangalore"
        print(" Location :" , self.location)
        self.__secret = None
    
    def get_secret(self):
        return self.__secret
        
    
    def set_secret(self, passedSecret):
        self.__secret = passedSecret
        