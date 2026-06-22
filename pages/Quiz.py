import streamlit as st
from datetime import date
import json
import random as r
if 'M' not in st.session_state:
    st.session_state['M']=0
if 'i' not in st.session_state:
    st.session_state['i']=1
if 'W' not in st.session_state:
    st.session_state['W']=0
if 'N' not in st.session_state:
    st.session_state['N']=0
c1,c2=st.columns([1.5,2.5])
with c1:
    pass
with c2:
    st.markdown("## Quiz System ##")
c3,c4,c5=st.columns([1,1,2])
with c3:
    st.write("Date:",date.today())
with c4:

    pass
with c5:
    with st.container(border=2):
        c6,c7=st.columns([1,3])
        with c7:
            st.write("Result Board")
        st.write("Correct Answer:",st.session_state['M'])
        st.write("Wrong Answer:",st.session_state['W'])
        st.write("Not Attempt Question:",st.session_state['N'])
def Quiz():
    with open("quiz.json","r") as f:
        a=json.load(f)
        k=r.choice(a)
        return k
if 'Q' not in st.session_state:
    st.session_state['Q']=Quiz()
with st.form("My"):
    st.write(st.session_state['i'],st.session_state['Q']["question"])
    MCQ=1
    for i in st.session_state['Q']["option"]:
        st.write(MCQ,i)
        MCQ+=1
    Answer=st.text_input("Enter Your Question:")
    if st.form_submit_button("Submit"):
            if Answer==st.session_state['Q']["correct"]:
                st.session_state['M']+=1
                st.success("Question is Successful Submit")
            else:
                st.session_state['W']+=1
    if st.form_submit_button("Skip"):
        st.session_state['N']+=1
        st.session_state['Q']=Quiz()
        st.session_state['i']+=1
        st.rerun()
    if st.form_submit_button("Next Question"):
        if Answer:
            st.session_state['Q']=Quiz()
            st.session_state['i']+=1
            st.rerun()
        else:
            st.warning("Enter Answer")