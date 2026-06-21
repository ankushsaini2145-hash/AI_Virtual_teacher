import streamlit as st
import random as r
st.markdown("## Number Gassing Game ##")
def Number():
    a=r.randrange(1,11)
    return a
if 'i' not in st.session_state:
    st.session_state['i']=Number()
user=st.number_input("Enter Number for integer:",min_value=0)
if st.button("Submit"):
    if st.session_state['i']==user:
        st.write("Correct Number")
        if st.button("Next"):
            st.rerun()
    else:
        st.write("Wrong")