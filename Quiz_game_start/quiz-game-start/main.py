from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]


def create(dict):
    q=dict["text"]
    a=dict["answer"]
    new=Question(q,a)
    return new

for i in question_data:

    question_bank.append(create(i))

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")