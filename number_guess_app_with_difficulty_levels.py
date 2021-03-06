import random
# first_number is constant so it is equals to 1.
# second_number is depends to the difficulty_level of user choice.
first_number = 1
second_number = 0
language = str(input(
    "Please choose a language for display: TR for Turkish, EN for English)..."))
if language.lower() == "en":
    difficulty_level = int(input("Please choose a difficulty level 1-2-3"))
    if difficulty_level == 1:
        second_number += 10
    elif difficulty_level == 2:
        second_number += 50
    elif difficulty_level == 3:
        second_number += 100
    else:
        raise ValueError ("Please choose between given range of 1-3")
    attempts_list = []
    def show_score():
        if len(attempts_list) <= 0:
            print("There is currently no high score, it's yours for the taking!")
        else:
            print("The current high score is {} attempts".format(min(attempts_list)))
    def start_game():
        random_number = int(random.randint(first_number, second_number))
        print("Hello traveler! Welcome to the game of guesses!")
        player_name = input("What is your name? ")
        wanna_play = input(
            "Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
        attempts = 0
        show_score()
        while wanna_play.lower() == "yes" or wanna_play.lower() == "ye" or wanna_play.lower() == "y":
            try:
                guess = input("Pick a number between {} and {} ".format(
                    first_number, second_number))
                if int(guess) < first_number or int(guess) > second_number:
                    raise ValueError(
                        "Please guess a number within the given range")
                if int(guess) == random_number:
                    print("Nice! You got it!")
                    attempts += 1
                    attempts_list.append(attempts)
                    print("It took you {} attempts".format(attempts))
                    play_again = input(
                        "Would you like to play again? (Enter Yes/No) ")
                    attempts = 0
                    show_score()
                    random_number = int(random.randint(1, 10))
                    if play_again.lower() == "no":
                        print("That's cool, have a good one!")
                        break
                elif int(guess) > random_number:
                    print("It's lower")
                    attempts += 1
                elif int(guess) < random_number:
                    print("It's higher")
                    attempts += 1
            except ValueError as err:
                print("Oh no!, that is not a valid value. Try again...")
                print("({})".format(err))
        else:
            print("That's cool, have a good one!")
    if __name__ == '__main__':
        start_game()
        
elif language.lower() == "tr":
    try:
        difficulty_level = int(input("L??tfen zorluk seviyesi se??iniz 1-2-3"))
        if difficulty_level == 1:
            second_number += 10
        elif difficulty_level == 2:
            second_number += 50
        elif difficulty_level == 3:
            second_number += 100
    except ValueError as ve:
        print("L??tfen belirtilen 1-3 zorluk seviyeleri aras??ndan se??im yap??n!")
    attempts_list = []
    def show_score():
        if len(attempts_list) <= 0:
            print(
                "En y??ksek skor bulunmamaktad??r, en y??ksek skorun yeni sahibi olmaya ??al??????n!")
        else:
            print("En d??????k deneme say??s?? {} deneme".format(min(attempts_list)))
    def start_game():
        random_number = int(random.randint(first_number, second_number))
        print("Say?? tahmin etme oyununa ho??geldin!")
        player_name = input("??sminiz nedir? ")
        wanna_play = input(
            "Merhaba, {}, say?? tahmin etmek ister misin? (Enter Evet/Hay??r) ".format(player_name))
        attempts = 0
        show_score()
        while wanna_play.lower() == "evet" or wanna_play.lower() == "yes":
            try:
                guess = input("{} ile {} aras??nda bir say?? tahmin ediniz...  ".format(
                    first_number, second_number))
                if int(guess) < first_number or int(guess) > second_number:
                    raise ValueError(
                        "L??tfen belirtilen {} ve {} say??lar?? aras??nda se??im yap??n??z!".format(first_number, second_number))
                if int(guess) == random_number:
                    print("Tebrikler bildiniz!")
                    attempts += 1
                    attempts_list.append(attempts)
                    print("Do??ru say??y?? bulman??z {} deneme kadar s??rd??! ".format(attempts))
                    play_again = input(
                        "Tekrar oynamak ister misin? (Enter Evet/Hay??r) ")
                    attempts = 0
                    show_score()
                    random_number = int(random.randint(1, 10))
                    if play_again.lower() == "hay??r" or play_again.lower()=="no":
                        print("Tekrar g??r??????r??z!")
                        break
                elif int(guess) > random_number:
                    print("Daha k??????k")
                    attempts += 1
                elif int(guess) < random_number:
                    print("Daha y??ksek")
                    attempts += 1
            except ValueError as err:
                print("Girdi??in de??er do??ru de??il, tekrar dene...")
                print("({})".format(err))
        else:
            print("Tekrar g??r??????r??z!")
    if __name__ == '__main__':
        start_game()
