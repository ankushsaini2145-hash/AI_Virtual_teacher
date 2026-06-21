import streamlit as st
import json
import nlp
c3,c4=st.columns([1,3])
with c3:
    pass
with c4:
    st.markdown("## AI Chatbot For Rules Based ##")
def Quiz():
    with open("chat.json","r") as f:
        a=json.load(f)
        return a
if 'data' not in st.session_state:
    st.session_state['data']=Quiz()
if 'A' not in st.session_state:
    st.session_state['A']=[]
c1,c2=st.columns([2.5,1.5])
a=st.chat_input("Enter Your Question:")
c=a
if a:
    a=nlp.clean(a)
    a=nlp.token(a)
    a=nlp.Remove(a)
    st.session_state['A'].append(a)
    for i in st.session_state['data']:
        if i in a:
            st.write("Answer:",st.session_state['data'][i])
            break
if a:
    with c1:
        pass
    with c2:
        st.write("User:",c)