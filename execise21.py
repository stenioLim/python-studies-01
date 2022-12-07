questions = [
    {
        "Question": "how much is 2 + 2",
        "Options" : ["1", "2", "4", "5"],
        "answer" : "4",
    },
    {
        "Question": "how much is 5 * 5",
        "Options" : ["25", "50", "10", "51"],
        "answer" : "25",
    },
    {
        "Question": "how much is 10 / 2",
        "Options" : ["4", "5", "2", "1"],
        "answer" : "5",
    },
]
answer_amount = 0
for question in questions:
    print("question:", question["Question"]) 

    print()

    option_1 = question["Options"]
    for i, option in enumerate(option_1):
        print(f"{i}) ",option)
    print()


    choose = input("choose an option: ")

    hit = False
    choose_int = None
    option_amount = len(option_1)

    if choose.isdigit():
        choose_int = int(choose)

    if choose_int is not None:
        if choose_int >= 0 and choose_int < option_amount:
            if option_1[choose_int] == question["answer"]:
                answer = True
    print()

    if answer:
        answer_amount += 1
        print("you are right")
    else:
        print("you missed")

    print()

print("You're right", answer_amount)
print("in ",len(questions)," questions")

