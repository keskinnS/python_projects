import random
import string

## first_number is constant so it is equals to 1.
## second_number is depends to the difficulty_level of users choice.
first_number = 1
second_number = 0

language = str(input("Please choose a language for display: TR for Turkish, EN for English)..."))
if language.lower() == "en":

        difficulty_level = int(input("Enter 1 for Easy mode, 2 for Normal mode and 3 for Hard mode..")) 

        while True:
            try:
                if difficulty_level == 1:
                    second_number += 10;
                    break
                elif difficulty_level == 2:
                    second_number += 50;
                    break
                elif difficulty_level == 3:
                    second_number += 100;
                    break
            except ValueError:
                    print("Invalid number to choose the difficulty level")
                    break

                
        
        
 

    