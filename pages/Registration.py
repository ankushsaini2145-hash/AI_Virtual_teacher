import streamlit as st
import json
if 'i' not in st.session_state:
    st.session_state['i']=[]
def File(b):
    with open("login.json","w+") as f:
        a=f.readlines()
        c=json.dumps(b)
        f.seek(0)
        f.write(c)
c1,c2=st.columns([1,3])
with c1:
    pass
with c2:
    st.markdown("## Registration Page ##")
with st.form("My"):
    user=st.text_input("Enter Username:")
    password=st.text_input("Enter Password",type="password")
    Profession=st.selectbox("Enter Your Profession:",["Student","Teacher","Admin"])
    if st.form_submit_button("Submit"):
        s={
            "user":user,
            "password": password,
            "profession": Profession
        }
        st.session_state['i'].append(s)
        File(st.session_state['i'])
        st.success("Submit")