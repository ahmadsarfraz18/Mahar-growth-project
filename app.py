# Streamlit Liberary...


import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge App", page_icon="✨✨")
st.title("Growth Mindset Challenge: Web App with Streamlit by Mahar Ahmad Sarfraz")

st.header ("🤷‍♂️ Welcome to your growth Journey")
st.write ("Embrace challenges, learn from mistakes and unlock your full potential this AI-powered app helps you to build a growth mindset with reflection, challenges, and achievements ✨")

# Quotes Section...abs

st.header ("Today's Growth Mindset Quote 👀")
st.write ("Success is not final 🙌, failure is not fatal: It is the courage to continue that counts.-Winston Churchill")

st.header ("What's your challenge today ?")
user_input = st.text_input ("Describe the challenge that you're facing")

# Conditions...abs

if user_input:
    st.success (f"🦾You're facing : {user_input}. Keep pushing forward towards your goal 🏆")
else: 
    st.warning ("Tell us about your challenge to get started")

# Reflection... 

reflection = st.text_area("Reflect on your learning")
reflection = st.text_area ("Write your reflection here ")

if reflection: 
    st.success (f"Great Insight! your reflection: {reflection}")
else:
    st.info ("Reflecting on your past experience helps you to grow! Share your difficulties")

# Achievements... 

st.header ("🏆 Celebrate your victory")
achievement = st.text_input ("Share something you have recently accomplished!")

if achievement: 
    st.success (f"Amazing you have achieved: {achievement}")

else:
    st.info ("Big or small, every achievement counts! Share anyone here 😍")

# Footer... 

st.write ("- - -")
st.write ("🎡 Keep believing in yourself! Growth is a journey, not the destination 👔")
st.write ("**Created with ❤❤❤ by Mahar Ahmad Sarfraz**")
