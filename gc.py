import gc

class Test:
    
    def __del__(self):
        print("Test object is garbage collected")
        
        

print("Getting threshold")
print(gc.get_threshold())

t=Test()
ref1 = t
del t


print("collect gen 0 objects")

gc.collect(0)
del ref1
gc.collect(1)
gc.collect(1)