
class QuizBrain:
    def __init__(self,q_list):
        self.question_no=0
        self.question_list=q_list
        self.score=0

    def next_question(self):
        current_question= self.question_list[self.question_no]
        self.question_no+=1
        user_answer=input(f"Q.{self.question_no}: {current_question.text} (True/False)")
        self.check_answer(user_answer,current_question.answer)

    def still_has_question(self):
        if(self.question_no+1==len(self.question_list)):
            return False
        else:
            return True

    def check_answer(self,user_answer,actual_answer):
        if(user_answer.lower()==actual_answer.lower()):
           print("you got it right")
           self.score+=1

        else:
            print("That's wrong")
        print(f"Te correct ans was: {actual_answer}")
        print(f"Your current score is: {self.score}/{self.question_no}")
        print()






input