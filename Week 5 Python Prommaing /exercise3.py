#QUESTION 1: What are the keys in the following dictionary?
MyDict = {"Color": "red", "name": "apple", "type": "fruit"}
print(MyDict.keys())

# answer : The kyes for the following dictionary are dict_keys(['Color', 'name', 'type'])
"Colors", 'name', and 'type'

#QUESTION 2: Extract all the keys of the dictionary below.

MyDict = {"Color": "red", "name": "apple", "type": "fruit"}
keys=MyDict.keys()
print(keys)

## answer : All the keys of the dictionary below that are extract
dict_keys(['color', 'name', 'type'])

## color , name , type are the keys of the dictionary that are extracted

#QUESTION 3: Iterate over the dictionary to print the corresponding key and value

MyDict = {"Color": "red", "name": "apple", "type": "fruit"}
keys=MyDict.keys()
print(MyDict.values()) , print(keys)

# answer print the correspondng key and value
dict_values (['red','apple', 'fruit'])
dict_keys(['Color','name','type'])
