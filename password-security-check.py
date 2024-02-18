#şifre güvenilirliği sorgulama
import streamlit as st
import string

sifre= st.text_input("Please enter your password: ")
bhl = list(string.ascii_uppercase)
khl = list(string.ascii_lowercase)
sl = list(string.digits)
cl = list(string.punctuation)

güç = 0

if len(sifre)>12:
    güç+=20
elif len(sifre)>8:
    güç+=10

for i in bhl:
    if i in sifre:

        güç+=20
        break
for i in khl:
    if i in sifre:

        güç+=20
        break
for i in cl:
    if i in sifre:

        güç+=20
        break
for i in sifre:
    if i.isdigit():

        güç+=20
        break




if güç <= 20:
    st.error("too weak")
elif güç<= 40:
    st.error("weak")
elif güç <= 60:
    st.error("medium")
elif güç <=80:
    st.success("good")
elif güç<=90:
    st.success("safe")
else:
    st.success("really safe:)")
    st.balloons()
