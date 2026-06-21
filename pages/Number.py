import streamlit as st
import random as r
c1,c2=st.columns([1,3])
with c2:
    st.markdown("## Number Gassing Game ##")
def Game(user):
    if st.button("Submit"):
        if st.session_state['i']==user:
            st.write("Correct Number")
            if st.button("Next"):
                st.rerun()
        else:
            st.write("Wrong")
c3,c4,c5=st.columns([.5,3,.5])
with c4:
    Level=st.selectbox("Select Your Level",["beginner","Midium","Pro"])
if 'a' not in st.session_state:
    st.session_state['a']=Level
st.write(st.session_state['a'])
if st.session_state['a']=="beginner":
    def Number():
        a=r.randrange(1,11)
        return a
    if 'i' not in st.session_state:
            st.session_state['i']=Number()
    user=st.number_input("Enter Choice Number(1 to 10)",min_value=0)
    Game(user)
elif st.session_state['a']=="Midium":
    def Number():
        a=r.randrange(1,51)
        return a
    if 'i' not in st.session_state:
        pass