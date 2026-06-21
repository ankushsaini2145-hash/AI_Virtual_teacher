import streamlit as st
st.title("Chatbot And Quiz System")
st.write("Intractive Chatbot and Quiz Learning Platform")

st.write("----------------------------")
c1,c2=st.columns(2)
with c1:
    st.markdown(" ## 🤖 Chat Bot ##")
    st.write("Ask questions and get AI responses.")
    if st.button(" Start Chat"):
        st.switch_page("pages/Chat.py")
with c2:
    st.markdown(" ## 📝 Quiz System ##")
    st.write("Test your knowledge with quizzes.")
    if st.button("Start Quiz"):
        st.switch_page("pages/Quiz.py")
c3,c4=st.columns(2)
with c3:
    st.markdown(" ## Login & Register ## ")
    st.write("Secure access for users.")
    c5,c6=st.columns([1,3])
    with c5:
        if st.button("Login"):
            st.switch_page("pages/Login.py")
    with c6:
        if st.button("Register"):
            st.switch_page("pages/Registration.py")
with c4:
    st.markdown(" ## Game Zone ## ")
    st.write("Play and learn with Fun Game")
    if st.button("Number Gassing Game"):
        st.switch_page("pages/Number.py")
    if st.button("Rock Paper Scissors Game"):
            st.switch_page("pages/Rockgame.py")
        