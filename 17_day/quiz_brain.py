class QuizBrain:

    def __init__(self, q_list):
        self.q_no = 0
        self.score = 0
        self.ques_list = q_list

    def has_question(self):
        return self.q_no < len(self.ques_list)

    def next_ques(self):
        curr_ques = self.ques_list[self.q_no]
        self.q_no += 1
        user_ans = input(f"Q.{self.q_no}:  {curr_ques.text}.  (True/False): ")
        self.check_answer(user_ans, curr_ques.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!!")

        print(f"The correct answer was : {correct_ans}")
        print(f"Your score is: {self.score}/{self.q_no}")
        print("\n")

