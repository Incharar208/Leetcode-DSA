#  Update / add an element to the dictionary

myDict = {'name': 'Edy', 'age': 26}
myDict['address'] = 'London'
print(myDict)

#  Traverse through a dictionary

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)

#  Searching a dictionary


def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(myDict, 27))

#  Delete or remove a dictionary

myDict.pop('name')




# sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}

print(sorted(myDict, key=len))



# METHODS:
firstValue = next(iter(hashMap.values())) # returns the first value of the hashMap

hashMap.values() # returns in the form of a list, all the values of a hashMap

for key, value in hashMap.items() # returns the key value pairs

hashMap = defaultdict(int)

# sorting hashMap based on its keys and values:
sortedHashMap = dict(sorted(hashMap.items(), key = lambda x:x[0], reverse = True))

x:x[0] # sorts based on keys
x:x[0] # sorts based on values

next(iter(sortedDict.keys())) # returns first key

