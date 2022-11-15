#quiz program

quiz = {
    "question1": {
        "question": "What is the capital of India",
        "answer": "Delhi"
    },

    "question2": {
        "question": "What is the capital of Assam",
        "answer": "Dispur"
    },

    "question3": {
        "question": "What is the capital of Telangana",
        "answer": "Hyderabad"
    },

    "question4": {
        "question": "What is the capital of Tamilnadu",
        "answer": "Chennai"
    },

    "question5": {
        "question": "What is the capital of Karnataka",
        "answer": "Bengaluru"
    },
}

score=0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('correct')
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")



    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is: "+ str(score))
        print("")
        print("")

print("You got " + str(score) + "out of 5 questions correctly")

print("Your percentage is " + str(int(score/5 * 100)) + "%")