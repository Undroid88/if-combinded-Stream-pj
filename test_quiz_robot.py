# test_quiz_robot.py

from quiz_robot import validate_non_empty_name, validate_answer

def test_validate_non_empty_name():
    assert validate_non_empty_name("Ridzy")
    assert not validate_non_empty_name("")
    assert not validate_non_empty_name("   ")

def test_validate_answer():
    assert validate_answer("Report it", "Report it")
    assert validate_answer("report it", "Report it")          # case-insensitive match
    assert validate_answer("  Report it  ", "Report it")      # trims whitespace
    assert not validate_answer("Ignore it", "Report it")