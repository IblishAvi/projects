# Lists in Python.

# names = ["Avi", "Naman", "Utkarsh", "ashutosh kumar"] #List of String
# print(names)
# names.append("Ananya") #Append module to add Ananya to list
# print(names)
# names.insert(1,"Rishu") #Insert function to insert at the specific end.
# print(names)
# friends = ["Avi", "Rohan", "Anmol", "Sukrit", "Ashutosh"]
# friends.extend(["beauty","Arti"])
# print(friends)
# names.pop(1)
# num = [24,12,22,25,27,32]
# num.reverse()
# print(num)
# num.sort()
# print(num)
# print(num)
# print(num[1:])
# print(num[1:4])

# Array in Python
# arr = [12,"Avi","lri"]
# print(arr)
# arr.pop()
# print(arr)
# arr.pop()
# print(arr)
# arr.insert(1,99)
# print(arr)
#
# arr.extend([85,54,46,76,98])
# print(arr)
# num =arr.copy()
# print(num)

# string in Python

name = "Avinash Kumar"
index = name.find("Kumar")
# print(index)

# print(name.capitalize()) # convert the string to capital case.
# print(name.lower()) # convert the string to lower case.
# print(name.__contains__("r")) # checks whether this value is present or not.
# print(name.endswith("r"))
# print(name.startswith("r"))
# print(name.count("a")) # checks  the occurrence of  provided string.
# print(name.isalnum())
# print(name.isspace())


# Tuple in Python
Profile = (
    ["Avi",24,"Male"],
    ["Ananya",22,"Female"],
    ["Rishu",25, "Male"]
)
# print(Profile)
# count1 = Profile[2].count("25")
# count2 = Profile[2].count(25)
# count1 = Profile[1].count("Ananya")
# print(Profile[1].index(22))
# print(Profile[1].index('Ananya'))
# print(Profile[1].index('Female'))
# print(count1)
# Dictionary in Python.

Profile ={
    "Name": "Avinash",
    "Age": 24,
    "Gender": "Male",
    "Occupation": "Job aspirant",
    "Hobby":"Watching Movies",
    "Qualification":"MCA"
}
print(Profile)

name =Profile["Name"] #Access the Name value from the Dictionary Using Key
print(name)
Age =Profile["Age"] #Access the Age value from the Dictionary Using Key
print(Age)
keys = Profile.keys() # This Prints the keys of the Dic.
value = Profile.values()

print(keys)
print(value)
