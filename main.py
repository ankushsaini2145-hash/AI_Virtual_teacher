import streamlit as st
if 'i' not in st.session_state:
    st.session_state['i']=[]
if 'Sum' not in st.session_state:
    st.session_state['Sum']=0
c1,c2=st.columns([1,3])
with c1:
    pass
with c2:
    st.markdown("## Expense Tracker ##")
with st.form("Form"):
    user=st.text_input("Enter Name:")
    category=st.text_input("Enter Expense Category (Food, Shopping, ext.):")
    date=st.date_input("Enter Expense Date:")
    description=st.text_input("Enter Description:")
    Amount=st.number_input("Enter Ammount for course:",min_value=0)
    if st.form_submit_button("Submit"):
        S={
            "User":user,
            "Category":category,
            "Date":date,
            "Description":description,
            "Amount":Amount
        }
        st.write(user)
        st.write(category)
        st.write(date)
        st.write(description)
        st.write(Amount)
        st.session_state['i'].append(S)
    for a in st.session_state['i']:
        st.write(a["User"])
        st.write(a["Category"])
        st.write(a["Date"])
        st.write(a["Description"])
        st.write(a["Amount"])
        Sum=0
        st.session_state['Sum']+=a["Amount"]
        st.write("Total Expense Amount is:",st.session_state['Sum'])