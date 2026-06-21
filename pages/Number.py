import streamlit as st
import random as r
c1,c2=st.columns([1,3])
with c2:
    st.markdown("## Number Gassing Game ##")
if 'Score' not in st.session_state:
    st.session_state['Score']=0
def Game(user):
    if st.button("Submit"):
        if st.session_state['i']==user:
            st.success("Correct Number")
            st.session_state['Score']+=1
            if st.button("Next"):
                st.session_state['i']=Number()
                st.rerun()
        else:
            st.write("Hint")
            if st.session_state['i']>user:
                st.write("Number is Big")
            elif st.session_state['i']<user:
                st.write("Number Is Less")
c6,c7=st.columns(2)
def Number():
    a=r.randrange(1,51)
    return a
if 'i' not in st.session_state:
    st.session_state['i']=Number()
user=st.number_input("Enter Choice Number(1 to 50)",min_value=0)
if st.button("Submit",key=1):
    if st.session_state['i']==user:
        st.write("Correct Number")
        if st.button("Next",key=1):
            st.rerun()
    else:
        st.write("Wrong")
Game(user)
with c6:
    pass
with c7:
    st.write("Your Score",st.session_state['Score'])