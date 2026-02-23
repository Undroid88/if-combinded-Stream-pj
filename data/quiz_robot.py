class QuestionRobot:
    def __init__(self, question, options, answer, category):
        self.question = question
        self.options = options
        self.answer = answer
        self.category = category


def user_input(name):
    return name.strip() != ""

def check_answer(user, correct):
    return user == correct