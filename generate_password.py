import random

def generate_string():
  uppercaseLetter1=chr(random.randint(65,90)) 
  uppercaseLetter2=chr(random.randint(65,90)) 
  lowercase_letter_one=chr(random.randint(97,122)) 
  lowercase_letter_two=chr(random.randint(97,122)) 
  first_number=random.randint(0,9) 
  second_number=random.randint(0,9) 
  first_symbol=chr(random.randint(33,63)) 
  second_symbol=chr(random.randint(33,63)) 

  generated_string = uppercaseLetter1 + uppercaseLetter2 + lowercase_letter_one + lowercase_letter_two + str(first_number) + str(second_number)+ first_symbol + second_symbol

  return generated_string

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

def main():
  pw=shuffle(generate_string())
  print(pw)


if __name__ == "__main__":
    main()