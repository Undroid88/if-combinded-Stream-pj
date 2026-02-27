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

# quiz_robot.py

def validate_non_empty_name(name: str) -> bool:
    """
    Returns True if 'name' contains any non-whitespace characters.
    """
    if name is None:
        return False
    return name.strip() != ""

def validate_answer(user_answer: str, correct_answer: str) -> bool:
    """
    Compares answers after trimming whitespace and ignoring case.
    """
    if user_answer is None or correct_answer is None:
        return False
    return user_answer.strip().casefold() == correct_answer.strip().casefold()