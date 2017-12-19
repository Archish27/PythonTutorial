xyz = [ i for i in range(5)] #List is actually presented in memory 
print(xyz)
xyz = ( i for i in range(5)) #Generator object
#Generators are not present in memory they are reference you can
#place into memory by iterating generators
print(xyz)

for p in xyz:
    print (p)

#xyz=[]
#for i in range(5):
#   xyz.append(i)

print(xyz)    

