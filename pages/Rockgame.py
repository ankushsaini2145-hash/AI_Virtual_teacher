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
if 'D' not in st.session_state:
    st.session_state['D']=0
if 'W' not in st.session_state:
    st.session_state['W']=0
if 'L' not in st.session_state:
    st.session_state['L']=0
if 'T' not in st.session_state:
    st.session_state['T']=0
c6,c7=st.columns([3,1])
with c7:
    with st.container(border=2):
        st.write("--Score Board--")
        st.write("Total Game:",st.session_state['T'])
        st.write("Draw Game:",st.session_state['D'])
        st.write("Loss Game:",st.session_state['L'])
        st.write("Win Game",st.session_state['W'])
c3,c4,c5=st.columns([.5,3,.5])
with c4:
    user=st.selectbox("Select Your Choice:",["Rock","Paper","Scissors"])
    user=user.lower()
    c6,c7=st.columns(2)
    with c6:
        if st.button("Submit"):
            if st.session_state['i']==user:
                st.write("Computer Choice:",st.session_state['i'])
                st.session_state['D']+=1
                st.write("Draw 🤝")
            elif st.session_state['i']=="rock" and user=="scissors" or st.session_state['i']=="scissors" and user=="paper" or st.session_state['i']=="rock" and user=="scissors":
                st.write("Computer Choice:",st.session_state['i'])
                st.session_state['L']+=1
                st.write("Lose 😔")
            else:
                st.write("Computer Choice:",st.session_state['i'])
                st.session_state['W']+=1
                st.write("Win 🏆")
    with c7:
        if st.button("Next"):
            st.session_state['i']=Game()
            st.session_state['T']+=1
            st.rerun()