class QuestionRobot:
    def __init__(self, question, options, answer, category):
        self.question = question
        self.options = options
        self.answer = answer
        self.category = category

    def check_answer(self, user, correct):
        return user == correct

def check_user_input(name):
    return name.strip() != ""


