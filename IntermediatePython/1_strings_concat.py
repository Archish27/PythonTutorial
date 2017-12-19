names = ["Jeff","Jill","Gary","Sam"]
for name in names:
    print("Hello There",name)
    #print("Hello ".join(['Hello There',name]))
    
print(', '.join(names))

import os
location_of_files = "C:\\Users\\Archish\\Desktop"
file_name = "license.txt"

print(location_of_files + "\\"+ file_name)

print(os.path.join(location_of_files,file_name))

with open(os.path.join(location_of_files,file_name)) as f:
    print(f.read())
