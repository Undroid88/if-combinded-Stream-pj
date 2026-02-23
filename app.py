import streamlit as st
import pandas as pd
from quiz_robot import QuestionRobot, check_name, check_answer

st.title("Welcome to my App")

# ASK FOR NAME
user_input = st.text_input("Your Name")
if user_input:
    st.write(f"Hello, {user_input.title()}")

if user_input and check_name(user_input):
     # LOAD QUESTIONS
    try:
        df = pd.read_csv("data/questions.csv")
    except FileNotFoundError:
        st.error("Questions file not found!")
        st.stop()

    # CONVERT QUESTIONS INTO ROBOTS
    questions = []
    for _, row in df.iterrows():
        q = QuestionRobot(
            row["question"],
            [row["option1"], row["option2"], row["option3"]],
            row["correct_answer"],
            row["category"]
        )
        questions.append(q)

    # QUIZ LOGIC
    if "index" not in st.session_state:
        st.session_state.index = 0
        st.session_state.score = 0

    if st.session_state.index < len(questions):

        q = questions[st.session_state.index]

        st.subheader(q.question)
        choice = st.radio("Pick one:", q.options)

        if st.button("Submit"):
            if check_answer(choice, q.answer):
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error(f"Incorrect. Correct answer: {q.answer}")

            st.session_state.index += 1
            st.rerun()

    else:
        st.success(f"You finished the quiz! Score: {st.session_state.score} / {len(questions)}")
        st.button("Restart", on_click=lambda: st.session_state.clear())