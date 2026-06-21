import streamlit as st
from datetime import date
import json
import random as r
if 'M' not in st.session_state:
    st.session_state['M']=0
c1,c2=st.columns([1.5,2.5])
with c1:
    pass
with c2:
    st.markdown("## Quiz System ##")
c3,c4,c5=st.columns([1,2,1])
with c3:
    st.write("Date:",date.today())
with c4:

    pass
with c5:
    st.write("Marks:",st.session_state['M'])
def Quiz():
    with open("quiz.json","r") as f:
        a=json.load(f)
        k=r.choice(a)
        return k
if 'Q' not in st.session_state:
    st.session_state['Q']=Quiz()
with st.form("My"):
    st.write("Q.",st.session_state['Q']["question"])
    MCQ=1
    for i in st.session_state['Q']["option"]:
        st.write(MCQ,i)
        MCQ+=1
    Answer=st.text_input("Enter Answer:")
    if st.form_submit_button("Submit"):
        if Answer==st.session_state['Q']["correct"]:
            st.session_state['M']+=1
            st.success("Question is Successful Submit")
    if st.form_submit_button("Next Question"):
            st.session_state['Q']=Quiz()
            st.rerun()