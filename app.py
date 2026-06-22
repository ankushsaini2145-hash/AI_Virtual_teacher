import streamlit as st
c7,c8=st.columns([.5,3.5])
with c8:
    st.title("Chatbot & Quiz System")
    st.write("Intractive Chatbot and Quiz Learning Platform")

st.write("----------------------------")
c1,c2=st.columns([1.9,2.1])
with c1:
    with st.container(border=2):
        st.markdown(" ## 🤖 Chat Bot ##")
        st.write("Ask questions and get AI responses.")
        if st.button("Start Chat"):
            st.switch_page("pages/Chat.py")
with c2:
    with st.container(border=2):
        st.markdown(" ## 📝 Quiz System ##")
        st.write("Test your knowledge with quizzes.")
        if st.button("Start Quiz"):
            st.switch_page("pages/Quiz.py")
c3,c4=st.columns(2)
with c3:
    with st.container(border=2):
        st.markdown(" ## Login & Register ## ")
        st.write("Secure access for users.")
        c5,c6=st.columns([1.5,2.5])
        with c5:
            if st.button("Login"):
                st.switch_page("pages/Login.py")
        with c6:
            if st.button("Register"):
                st.switch_page("pages/Registration.py")
        st.write("\n")
        st.write("\n")
with c4:
    with st.container(border=2):
        st.markdown(" ## Game Zone ## ")
        st.write("Play and learn with Fun Game")
        if st.button("Number Gassing Game"):
            st.switch_page("pages/Number.py")
        if st.button("Rock Paper Scissors Game"):
            st.switch_page("pages/Rockgame.py")