import traceback

class InvalidAgeException(Exception):
    pass

class Member:
    def __init__(self, membername, memberage):
        validateAge(memberage)
        self.membername = membername
        self.memberage = memberage
    
    def validateAge(age):
        if age < 18:
            raise InvalidAgeException("Only person above 18 is allowed to enter")
    
class Club:
    def becomeMember:
        
try:
    inputAge = int( input("Please enter your age:"))
    validateAge(inputAge)
    print(" your age is ", inputAge, " , you are allowed to enter")
except InvalidAgeException as ageexep:
    print(f" entry restricted: {ageexep}")
except:
    traceback.print_exc()