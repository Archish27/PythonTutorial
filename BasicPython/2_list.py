grocery_list = ['Juice','Tomatoes',
                'Potatoes','Bananas']

print('First Item',grocery_list[0])
grocery_list[0]="Green Juice"
print(grocery_list[0:3])
other_events = ['Wash car','Pickup Kids',
              'Cash check']

to_do_list=[other_events,grocery_list]
print(to_do_list) #List within List


grocery_list.append("Onions")

grocery_list.insert(1,"Pickle")

print(grocery_list)

grocery_list.remove("Green Juice")

print(grocery_list)

grocery_list.sort()
print(grocery_list)
grocery_list.reverse()
print(grocery_list)

del grocery_list[4]
print(grocery_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2[0]))

#NOTE :
#List can be changed according to requirement
