# QUESTION 1: What would be the output of the following code block?

count = 4
print(count == 2)
print(count != 4)
print(count > 4)
print(count < 6)

## the out put of the following code are as follow:
False
False
False
True

# QUESTION 2: What would be the output of the following code block?
def functionName():

color = 'red'
category = 'fruit'

if color == "red" and category == "fruit":
 print ("We have an Apple")

if color == "red" and category == "vegetable":
 print ("We have tomatoes")

 ## output will be as follow :
 We have an output

# QUESTION 3: What would be the output of the following code block?

requested = ['blueberry', 'banana']
fruits = ['apple', 'banana', 'watermelon', 'kiwi', 'rasberry']

if requested not in fruits:
    print("Sorry, We don't have bananas in stock. Please review your order!")

else:
    print("Order is placed!")

# Output of the following block is

Sorry, We don't have bannas in stock. Please review your order!


   #QUESTION 4: What would be the output of the following code block?

 scores1 =(1,2,3)
 scores2 =(1,2,3)
 print(scores1 = scores2)

scores1 = [1,2,3]
scores2 = [1,2,3]

print(scores1 == scores2)


#The output that comes out is
True

#QUESTION 5: What would be the output of the following code block? Learn about 'is' operator.

scores1 = [1,2,3]
scores2 = [1,2,3]

print(scores1 == scores2)
print(scores1 is scores2)

# The output of the following code block is
True
False


#QUESTION 6: Print the following pattern using for loops:
## Q3: What would be the output of the following code block?
scores = [67, 90, 89, 78, 99, 100]
for scores  in  [67, 90, 89, 78, 99, 100]:
 print (scores)
