from data import question_data


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_bank = []
for key in question_data:
    question_text = key["text"]
    question_answer = key["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        for question in self.question_list:
            input1 = input(question.text)
            if input1 == question.answer:
                print("good")
            self.question_number += 1


quiz = QuizBrain(question_bank)
quiz.next_question()
