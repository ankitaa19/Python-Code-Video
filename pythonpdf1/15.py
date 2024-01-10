class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self, user_answers):
        score = 0
        for i, question in enumerate(self.questions, start=1):
            print("\nQuestion {}: {}".format(i, question.text))
            for j, option in enumerate(question.options, start=1):
                print("{}. {}".format(j, option))

            user_answer = int(input("Your answer (enter the option number): "))
            if user_answer == question.correct_option:
                score += 1

        return score

class User:
    def __init__(self, name):
        self.name = name

question1 = Question("What is the capital of India?", ["Delhi", "Mumbai", "Pune", "Hyderabad"], 1)
question2 = Question("Which programming language is this program written in?", ["Python", "Java", "C++", "JavaScript"], 1)

quiz = Quiz("General Knowledge", [question1, question2])

user1 = User("Alice")

user_answers = {
    question1: 1,
    question2: 1,
}

user1_score = quiz.take_quiz(user_answers)

print("\n{}'s Quiz Results:".format(user1.name))
print("Score: {}/{}".format(user1_score, len(quiz.questions)))