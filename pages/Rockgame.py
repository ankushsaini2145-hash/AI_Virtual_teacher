import streamlit as st
import random as r
c1,c2=st.columns([.5,3.5])
with c2:
    st.title("Rock Paper Scissors Game")
with c1:
    pass
def Game():
    a=["rock","paper","scissors"]
    return r.choice(a)
if 'i' not in st.session_state:
    st.session_state['i']=Game()
c3,c4,c5=st.columns([1,2,1])
with c4:
    user=st.text_input("Enter choice(Rock Paper Scissors):")
    user=user.lower()
    c6,c7=st.columns(2)
    with c6:
        if st.button("Submit"):
            if st.session_state['i']==user:
                st.write("Computer Choice:",st.session_state['i'])
                st.write("Draw 🤝")
            elif st.session_state['i']=="rock" and user=="scissors" or st.session_state['i']=="scissors" and user=="paper" or st.session_state['i']=="rock" and user=="scissors":
                st.write("Lose 😔")
            else:
                st.write("Computer Choice:",st.session_state['i'])
                st.write("Win 🏆")
    with c7:
        if st.button("Next"):
            st.session_state['i']=Game()
            st.rerun()