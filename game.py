import streamlit as st
import random as r
st.title("Rock Paper Scissors Game")
def Game():
    a=["rock","paper","scissors"]
    return r.choice(a)
if 'i' not in st.session_state:
    st.session_state['i']=Game()
st.session_state['i']=Game()
user=st.text_input("Enter choice:")
user=user.lower()
if st.button("Submit"):
    if st.session_state['i']==user:
        st.write("Computer Choice:",st.session_state['i'])
        st.write("Game Draw")
    elif st.session_state['i']=="rock" and user=="scissors" or st.session_state['i']=="scissors" and user=="paper" or st.session_state['i']=="rock" and user=="scissors":
        st.write("Computer Win")
        st.write(st.session_state['i'])
    else:
        st.write("Computer Choice:",st.session_state['i'])
        st.write("User Win")
    if st.button("Next"):
        st.session_state['i']=Game()
        st.rerun()