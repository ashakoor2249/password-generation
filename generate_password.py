import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercase_letter_one=chr(random.randint(97,122)) #Generate a random lowercase letter based on the ASCII code)
lowercase_letter_two=chr(random.randint(97,122)) #Generate a random lowercase letter based on the ASCII code)
first_number=random.randint(0,9) #Generate a random number.
second_number=random.randint(0,9) #Generate a random number
first_symbol=chr(random.randint(33,63)) #Generate a random symbol
second_symbol=chr(random.randint(33,63)) #Generate a random symbol


#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercase_letter_one + lowercase_letter_two + str(first_number) + str(second_number)+ first_symbol + second_symbol # + ....
password = shuffle(password)

#Ouput
print(password)
