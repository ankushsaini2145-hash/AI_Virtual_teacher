import streamlit as st
import json
c1,c2,c3=st.columns(3)
with c1:
    pass
with c2:
    st.markdown("## Login Page ##")
with c3:
    pass
def Login():
    with open("login.json","r") as f:
        a=json.load(f)
        return a
if 'i' not in st.session_state:
    st.session_state['i']=Login()
with st.form("My Form"):
    User=st.text_input("Enter Username:")
    Password=st.text_input("Enter Password:",type="password")
    Profession=st.selectbox("Enter Profession:",["Student","Teacher","Admin"])
    if st.form_submit_button("Submit"):
        for i in st.session_state['i']:
            if i["user"]==User:
                if i["password"]==Password:
                    if i["profession"]==Profession=="Admin":
                        st.write("Admin")
                        st.success("Successful Login")
                    elif i["profession"]==Profession=="Student":
                        st.write("Student")
                        st.success("Successful Login")
                    elif i["profession"]==Profession=="Teacher":
                        st.write("Teacher")
                else:
                    st.warning("Password Wrong")