user_name=input("Enter your Username:") #ask the user for username
password=input("Enter a password:") #ask the user for password
#string  variables to check
specailChars="'[_#$%^&*()<>?/\|}{~:]'" #special characters defined
smallAlpha='abcdefghijklmnopqrstuvwxyz' #small alphabets
bigAlpha='ABCDEFGHIJKLMNOPQURSTUVWXYZ' #capital 
digts='1234567890' #digits
invalidCharacters='!@+=-' #invalid character feel free to add the characters you want

import random #random library
def random_index(str): #to get the random index value in the string
    a=random.randint(0,len(str)) #get the index value with in the string
    return a #return that index value when called
def random_letter_small(): #function to choose one  letter form small character
    return(random.choice(smallAlpha)) #choosing one from the string
def random_letter_big():#function to choose one  letter form big character
    return(random.choice(bigAlpha))#choosing one from the string
def random_letter_digit():#function to choose one  letter form digts character
    return(random.choice(digts))#choosing one from the string
def random_letter_special():#function to choose one  letter form specail character
    return(random.choice(specailChars))#choosing one from the string

list=[] #list to store the counts
#intitalizing the count variables
upperCount=0
lowerCount=0
digtsCount=0
specialCount=0
invalidCount=0
#iterationg over the elements of password
for i in password:
    if i.isupper(): #checking if element is uppercase
        upperCount+=1 #increment it
    elif i.islower():#checking if element is lower
        lowerCount+=1#increment it
    elif i.isdigit():#checking if element is digit
        digtsCount+=1#increment it
    elif i in specailChars:#checking if element is special character
        specialCount+=1#increment it
    else:
        invalidCount+=1#increment it
if len(password)<9: #to store as 0 in the list if length of the password is 9
    list.append(0) #adding that 0
else: #else conditing
    list.append(len(password)) #adding the length of password
# adding all the counts to the list
list.append(len(password))
list.append(upperCount)
list.append(lowerCount)
list.append(digtsCount)
list.append(specialCount)
list.append(invalidCount)

exist=False #boolear
if user_name in password:#Checkig if the password is in username
    exist=True #if yes set exist as true

newtemp="" #new string
if invalidCount>0: #checking if invalid count is greater than 0
    for i in password: #iterating over the password
        if i in invalidCharacters: #if the eleemnt is invalid character
            continue #don't do anyting
        else: #else
            newtemp=newtemp+i #add that character to new string 
    print("* New password with invalid characters removed:",newtemp)#print it
    password=newtemp #assign that string to password
#printing the counts 
print("* length of the password:",len(password))
print("* username is part of password:",exist)
print("* # of uppercase characters in the password:",upperCount)
print("* # of lowercase characters in the password:",lowerCount)
print("* # of digits in the password:",digtsCount)
print("* # of special characters in the password:",specialCount)
print("* # of invalid characters in the password:",invalidCount)
# if list contains 0 in their elements
if 0 in list:
    print("Password is invalid") #print the password is invalid

choice=input("Enter woruld you like us to fix your password for you?") #asking the user
if choice.lower()=='yes': #if user enters yes
    #condition if the password in username
    if exist==True: 
        index_val=random_index(password) #get some random index value with in the string
        special=random_letter_small() #get some random small letter
        password=password[:index_val]+special+password[index_val:] #add that random letter at the random index value
        print("* Username is in password -inserting random character to remove it:",password) #print the updated password


    if  upperCount==0: #if there are no upper case alphabets
        index_val=random_index(password)#get some random index value with in the string
        special=random_letter_big() #choose an random upper case letter
        password=password[:index_val]+special+password[index_val:]#add that random letter at the random index value
        print("* Adding a random uppercase character at a random postioon:", password)#print the updated password

    if  lowerCount==0: #if there are no lower case alphabets
        index_val=random_index(password)#get some random index value with in the string
        special=random_letter_small() #get a random alphabet
        password=password[:index_val]+special+password[index_val:]#add that random letter at the random index value
        print("* Adding a random lowercase character at a random postioon:", password)#print the updated password

    if digtsCount==0: #fi there are no digits in the password
        index_val=random_index(password)#get some random index value with in the string
        special=random_letter_digit() #pick a random digit
        password=password[:index_val]+special+password[index_val:]#add that random letter at the random index value
        print("* Adding a random digt character at a random postion:",password)#print the updated password

    if specialCount==0: #if there are no specail chars 
        index_val=random_index(password)#get some random index value with in the string
        special=random_letter_special() #pick a random special char
        password=password[:index_val]+special+password[index_val:]#add that random letter at the random index value
        print("* Adding a random special character at a random positon:", password)#print the updated password

    if len(password)<9: #if the password length is less than 9
        index_val=random_index(password)#get some random index value with in the string
        special=random_letter_small() #pick a random small later
        password=password[:index_val]+special+password[index_val:]#add that random letter at the random index value
        print("* Adding a random letter to meet minimal length:", password) #print the updated password
    print("Your new password is ",password) #print the final password
