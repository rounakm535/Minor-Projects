from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_txt = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_txt, question_ans)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.has_question():
    quiz.next_ques()

print("You have completed the quiz ")
print(f"Your total score is: {quiz.score}/{quiz.q_no}")