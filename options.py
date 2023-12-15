questions = (
    "Which is star: ",
    "Which person owns F.B: ",
    "Which person has the most Subs on Yt : "
)

options = (
    ("A. Earth ", " B. Mercury", "C. Sun", "D.Orange"),
    ("A.MarkZuckerBurg", "B.Me", "C.ImranKhan", "D.No one"),
    ("A.GeoNews", "B.PewDiePie", "C.Mrbeast", "D.Levinho")
)

answers = ("C", "A", "C")

retry = True

while retry:
    guesses = []
    score = 0
    question_no = 0

    print("----- Quiz -----")

    for question in questions:
        print("\n---------------------")
        print(f"{question}")
        for option in options[question_no]:
            print(option)
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_no]:
            score += 1
            print("CORRECT")
        else:
            print("INCORRECT")
            print(f"The correct answer is {answers[question_no]}")

        question_no += 1

    print("\n----- Results -----")
    print("Correct Answers:", answers)
    print("Your Answers:", guesses)

    final_score = int(score / len(questions) * 100)
    print(f"\nYour score is {final_score}%")

    retry = input("\nDo you want to retry the quiz? (yes/no): ").lower() == "yes"

print("Thank you for playing!")
