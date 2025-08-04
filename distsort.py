# user profile by sorting them based on name


#UserProfile Params..
#userId,
#userName,
#userContact


class UserProfile:
    
    def __init__(self,userId, userName, userContact):
        self.userId = userId
        self.userName = userName
        self.userContact = userContact
        
    def __str__(self):
        return f"{self.userId} / {self.userName} / {self.userContact}"
        
user1 = UserProfile(1, "Nikhil", 9845678323)
user2 = UserProfile(2, "Vishist", 98678734895)
user3 = UserProfile(3, "Ganesh", 9874454232)

#print(user1)

userDist = { "NY": user1, "LON": user2, "SFO": user3}

#print(type(userDist))



#print(userDist)
sortedUser = sorted(userDist.items(),key=lambda x: x[1].userName)

#print(sortedUser)

for id,u in sortedUser:
    print(u)
    print(id)


#print(sortedUser)