#NOTE
#You cannot change tuple once it is initialized

pi_tuple=(3,4,4,1,2,3)
new_list = list(pi_tuple)
new_tuple = tuple(new_list)

print(len(new_tuple))
print(min(new_tuple))
print(max(new_tuple))
