import streamlit as st
import random as r
c1,c2=st.columns([1,3])
with c2:
    st.markdown("## Number Gassing Game ##")
if 'Score' not in st.session_state:
    st.session_state['Score']=0
if 'N' not in st.session_state:
    st.session_state['N']=0
if 'A' not in st.session_state:
    st.session_state['A']=0
c6,c7=st.columns(2)
def Number():
    a=r.randrange(1,51)
    return a
if 'i' not in st.session_state:
    st.session_state['i']=Number()
user=st.number_input("Enter Choice Number(1 to 50)",min_value=0)
c11,c12=st.columns(2)
with c11:
    if st.button("Submit"):
        if st.session_state['i']==user:
            st.success("Correct Number")
            st.session_state['Score']+=1
        else:
            if st.session_state['i']>user:
                st.write("Number Is Big")
                st.session_state['N']+=1
            elif st.session_state['i']<user:
                st.write("Number Is Less")
                st.session_state['N']+=1
with c12:
    if st.button("Next"):
        st.session_state['i']=Number()
        st.session_state['A']+=1
        st.rerun()
with c6:
    pass
with c7:
    with st.container(border=2):
        c8,c9=st.columns([1,3])
        with c9:
            st.write("Score Board")
        st.write("Win Game",st.session_state['Score'])
        st.write("Attampt Game:",st.session_state['N'])
        st.write("Total Game:",st.session_state['A'])