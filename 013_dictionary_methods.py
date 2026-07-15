marks = {
    "Nishad" : 80,
    "Rahi" : 100,
    "A" : 60,
    "B" : 70
}

d = {} #empty dictionary

print(marks.items()) #it will return all the items in the dictionary as a list of tuples
print(marks.keys()) #it will return all the keys in the dictionary as a list
print(marks.values()) #it will return all the values in the dictionary as a list
print(marks.update({"C" : 90})) #it will update the dictionary with the new key-value pair and return None 
print(marks.get("Nishad")) #it will return the value of the key "Nishad" which is 80