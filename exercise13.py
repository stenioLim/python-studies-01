import os

secret_word = "house"
letter_win = ""
number_of_attempts = 0
while True:

    letter = input("type your letter: ")
    number_of_attempts += 1
    # checking how many letters were typed
    if len(letter) > 1:
        print("Type only one letter")
        continue
    
    if letter in secret_word:
        letter_win += letter

    #
    formed_word = ""
    for secret_letter in secret_word:
        if secret_letter in letter_win:
            formed_word += secret_letter
        else: 
            formed_word += "*"
    print("The formed word is: ",formed_word)

    if formed_word == secret_word:
        os.system("clear")
        print("Win")
        print("The secret word is:", secret_word)
        print("number of attemps is: ", number_of_attempts)
    
        letter_win = ""
        number_of_attempts = 0
    