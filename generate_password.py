import csv
import random

class PasswordManager:
  def __init__(self):
    self.csv_path="pw.csv"
  
  def generate_pw(self):
    uppercaseLetter1=chr(random.randint(65,90)) 
    uppercaseLetter2=chr(random.randint(65,90)) 
    lowercase_letter_one=chr(random.randint(97,122)) 
    lowercase_letter_two=chr(random.randint(97,122)) 
    first_number=random.randint(0,9) 
    second_number=random.randint(0,9) 
    first_symbol=chr(random.randint(33,63)) 
    second_symbol=chr(random.randint(33,63)) 

    generated_string = uppercaseLetter1 + uppercaseLetter2 + lowercase_letter_one + lowercase_letter_two + str(first_number) + str(second_number)+ first_symbol + second_symbol

    tempList = list(generated_string)
    random.shuffle(tempList)
    return ''.join(tempList)
  
  def save_password(self, application_name, pw):
    with open(self.csv_path, 'a', newline='') as file:
      password_writer=csv.writer(file, delimiter=',')
      password_writer.writerow([application_name, pw])
    return True

def main():
  password_manager=PasswordManager()
  while True:
    print("enter 'q' anytime to exit...")
    if(application_name := input("Enter the name of the application you want to create a password for: "))=='q':
      break

    pw=password_manager.generate_pw()
    print(f'New password for "{application_name}" is {pw}')

    if (response := input("Would you like to save this new password? (y/n): "))=='y':
      password_manager.save_password(application_name, pw)
      print(f'{pw} saved successully.')
    elif response=='q':
      break


if __name__ == "__main__":
    main()