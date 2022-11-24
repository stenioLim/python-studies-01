
phrase = "I'm studying all the time and working all the time, either way I'm going to win"

i = 0 
amount_that_appears_most_often = 0
letter_that_appears_more_times = ""
while i < len(phrase): 
    phrase_now = phrase[i]

    if phrase_now == " ":
        i += 1
        continue

    h_times_letters_appear = phrase.count(phrase_now)

    if amount_that_appears_most_often < h_times_letters_appear:
        amount_that_appears_most_often = h_times_letters_appear
        letter_that_appears_more_times = phrase_now


    
    i += 1


print(
    " The letter that appears most often was " 
    f"{letter_that_appears_more_times} appeared "
    f"{amount_that_appears_most_often} x"

)
