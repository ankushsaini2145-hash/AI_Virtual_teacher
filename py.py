import streamlit as st
from datetime import datetime
import time
st.markdown("## Timer  ##")
if 'i' not in st.session_state:
    st.session_state['i']=datetime.now()
d=st.number_input("Set Timer")
if 'd' not in st.session_state:
    st.session_state['d']=d
c=st.empty()
a=st.empty()
while 1<=d:
    b=datetime.now()
    c.write(b)
    a.write(b-st.session_state['i'])
    time.sleep(1)
    d-=1