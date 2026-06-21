import streamlit as st
st.markdown("## Chatbot And Quiz System ##")
st.write("Intractive Chatbot and Quiz Learning Platform")

st.write("----------------------------")
c1,c2=st.columns(2)
with c1:
    st.write("🤖 Chat Bot")
    st.write("Ask questions and get AI responses.")
    if st.button(" Start Chat"):
        st.switch_page("pages/Chat.py")
with c2:
    st.write("📝 Quiz System")
    st.write("Test your knowledge with quizzes.")
    if st.button("Start Quiz"):
        st.switch_page("pages/Quiz.py")
c3,c4=st.columns(2)
with c3:
    st.write("Login & Registration")
    st.write("Secure access for users.")
    c5,c6=st.columns([1.5,2.5])
    with c5:
        if st.button("Login"):
            st.switch_page("pages/Login.py")
    with c6:
        if st.button("Registration"):
            st.switch_page("pages/Registration.py")
with c4:
    st.write("Game")
    c7,c8=st.columns(2)
    with c7:
        if st.button("Number Gassing Game"):
            st.switch_page("pages/Rockgame.py")
