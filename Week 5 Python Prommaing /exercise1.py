# #QUESTION 1: What is 84 / 12 + 2 * 2 ?


a = 84
b = 12
c = 2

print (a/b + c * c)

# #QUESTION 2: What is the type of the answer variable in this expression ?

answer = 12/ 4
print(type(answer))

# QUESTION 3:  What is the value of num?

num1=  2
num2= 5 * 10

print(num1)
print(num2)

# # QUESTION 4: What would this expression evaluate to?

alist1 = ("tom")
alist2= 1
alist3= ("tom" + "1"),

print (alist3)

# This part took a while but was able to figure it out the output will be tom1

# # QUESTION 5:  What would this expression evaluate?


a=6
b=4

print (6+4)

 # # QUESTION 6:What would be the output of MyString[5:12]

MyString = "Data Science with Harshit"
alist4= ("MyString",5, 12)
print("%s 5,12" % MyString)

# # # QUESTION 7: What would be the output of MyString[5:]

MyString = "Data Science with Harshit"
alist5= ("MyString",5)
print("%s 5" % MyString)

## out will be Data Science with Harshit 5
## # QUESTION 8:  What would be the output of MyString[5::2]

MyString = "Data Science with Harshit"
alist6= ("MyString",5,2)
print("%s 5,2" % MyString)

# Data Science with Harshit 5,2 is the output
 ### QUESTION 9: Is there any 'go' in MyString if yes, at what index?
"You should go to your home!
## this section took long to figure it out

myString = "You should go to your home"
if myString == ("You should go to your home"):
 print("You should go to your home! Go")

else:
    print ("What index!")


    print ("Stay, do not go home!")

    # You should go to your home! GO is the output that comes out

## # QUESTION 10: Evaluate the following expression and convert it to string object?
18 + 19 * 11

answer= 18 + 19 * 11
answer_string= str(answer)
print(answer_string)

# the evaluate result is 227
## # QUESTION 11: Replace Harshit with your name in the statement below!
MyString1 = "Data Science with Paul"
print(MyString1)

# Data Science with Paul is the output
## # QUESTION 12: Use the split() function to extract all the words of MyString in a list

MyString = "Data Science with Harshit"
x= MyString.split()
print (x)

# ['Data', 'Science', 'with', 'Harshit'] is thee output
## # QUESTION 13: Extract the last element of the list without counting
MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87]
print(MyList[3:5])

# When extracting result will be ["tom", "red"]

### QUESTION 14:  What is the length of the list below?
MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87]
len(MyList)
print(len(MyList))

## # QUESTION 15: Extract all the elements from 2nd index to 6th index
MyList =[23, 43, 56, 'tom', 'red', 65, 89, 90, 87]

print(MyList[2:6])

## QUESTION 16:  Extract all the elements except last 2 using slicing
MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87]
print(MyList[-9:-2])

### QUESTION 17: Are lists mutable? (Yes/No)
## ask # QUESTION:

if  "yes" == True:
   print("Yes_ lists_mutable")

else:
    print ("No_lists_mutable")
    print("lists mutable sovled")

## This one took long to solve try it with bool and wasn't getting it
## Decide to use if and else
## out put will No list mustable

## QUESTION 18 : Sort the below list using the in-built list class function:
MyList = [23, 43, 56, 65, 89, 90, 87]
MyList.sort()
print (MyList)

# QUESTION 19: Delete 'tom' and 'red' from the list using remove() function
MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87]
MyList.remove ("tom") , MyList.remove('red')
MyList.sort()
print(MyList)

# QUESTION 20: Tuples are mutable(True/False)

if  "yes" == True:
   print("Yes_ lists_mutable")

else:
    print ("False not Mutable")

    print ("Question has been answer if tuples are mutable")

# This one took a long time will need to review, but i got as final result False not mutable


# QUESTION 21: From a tuple (23, -1, 34, [1 , 3] , 90), extract 3
#tuples

tuple1=(23,-1,34)
tuple2=[1,3]
tuple3=(90)






#Question 21 took a long time I extract 3 tuples like this. Will need classification and review to make sure I'm right
# Code runs perfectly



# QUESTION 22: What is right method to clone a list? Create a clone the list below. `Imp` (Hint: slicing)
MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87]

# method to clone a list

MyList = [23, 43, 56, 'tom', 'red', 65, 89, 90, 87][:]
MyList2= (MyList[:])
print(MyList2)
print (MyList)



#Question 22 took longer but went with this 
