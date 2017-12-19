#NOTE
#You can change dictionary but you cannot join two dictionaries

super_villans = {'Fiddler' : 'Issac Bowin',
                 'Captain Cold' : 'Leonard Snart',
                 'Weather Wizard':'Sam Scudder',
                 'Pied Piper':'Thomas Peterson'}

print(super_villans["Pied Piper"])

del super_villans["Pied Piper"]

super_villans["Fiddler"]="John Martin"

print(super_villans)


print(super_villans.get("Pied Piper"))
print(super_villans.keys())
print(super_villans.values())

