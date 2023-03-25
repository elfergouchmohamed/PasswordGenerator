#Import libraires

from random import sample
import string 

#Print welcome message 

print('Welocome to Password generator !')

#Demand the length of password 

length = int(input('Enter length of your password :'))

#build the data 

upperC = string.ascii_uppercase
lowerC = string.ascii_lowercase
numbers = string.digits
specialC = string.punctuation

#create password list 

passL = upperC + lowerC + numbers + specialC

#use random 

tmp = sample(passL,length)

#print the password 

password = "".join(tmp)
print(password)