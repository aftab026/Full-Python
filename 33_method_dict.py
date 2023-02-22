myDict = {
    "fast": "In a Quick Manner",
    "aftab": "A Code",
    "marks": [1,2,3],
    "anotherdict":{'Aftab':'player'},
    1:2
}
#  dictionary method
# print(list(myDict.keys())) # prints the keys of the dictionary
# print(myDict.values()) # prints the value of the dictionary
# print(myDict.items()) # print the (key, value ) for all contents of the dictionary
print(myDict)
updateDict = {
    "Lovish": "Friend"
}
myDict.update(updateDict) #Updates the dictinoary by adding key-value pairs free updateDict
print(myDict)

print(myDict.get("aftab")) # prints value associated with key "aftab"
print(myDict["aftab"])# prints value associated with key "aftab"

# the difference between. get and[] syntax in dictionaries?
print(myDict.get("aftab2")) # returns none as harry2 is not present in the dictinoary
# print(myDict["aftab2"])# throw an error as harry is not present in the dictionary