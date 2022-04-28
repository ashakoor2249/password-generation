This program generates a random password of eight characters. Each time the program runs a new password is generated utilzing random. The password has two upper case letters, two lower case letters, two digits between 0 and 9, and 2 special characters.

Major changes was made to the program. A class, PasswordManager was defiend to better organize the program.

The creation of the random password was condensed into one method called generate_pw

THe csv module was imported in order to create a csv file where the generated passwords along with their associated application could be stored.

The user is able to create as many passwords as they want utilizng a while loop in main.
