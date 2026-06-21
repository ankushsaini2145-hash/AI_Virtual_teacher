import json
import random as r
import streamlit as st
# Question and Answer file Read for using File Handling
def Chat(b):
    with open("chat.json","r") as f:
        a=json.load(f)
        for i in a:
            if i in b:
                return a[b]
            else:
                return "I am learning"
# Quiz File 
def Quiz():
    with open ("quiz.json","r") as f:
        Question=json.load(f)
        Mark=0
        # Random Question Genrate for Random Module Use
        c=r.choice(Question)
        Q=1
        for i in c:
            st.write(f"{Q}. {c["question"]}")
            MCQ=1
            Q+=1
            for b in c["option"]:
                st.write(f"{MCQ}. {b}")
                MCQ+=1
                if st.button("submit"):
                    anser=st.text_input("Enter Answer:",key=f"text_input_{i+1}")
                    if anser==c["correct"]:
                        Mark+=1
                        st.write("correct answer")
                    else:
                        st.write("Correct Answer is: ",c["correct"])