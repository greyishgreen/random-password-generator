import streamlit as st
import string
import random

uzunluk = int(st.slider("Please choose the password length", 6, 20, value=8))

st.write("Characters to be used:")
bh = st.checkbox("ABC", value=True)
kh = st.checkbox("abc", value=True)
s = st.checkbox("123", value=True)
c = st.checkbox("#&!", value=True)

checkbox_işaretlenen=[]


bhl = list(string.ascii_uppercase)
khl = list(string.ascii_lowercase)
sl = list(string.digits)
cl = list(string.punctuation)

kl = []

if bh:
    kl += bhl
    checkbox_işaretlenen.append(bhl)
if kh:
    kl += khl
    checkbox_işaretlenen.append(khl)
if s:
    kl += sl
    checkbox_işaretlenen.append(sl)
if c:
    kl += cl
    checkbox_işaretlenen.append(cl)


a = uzunluk - len(checkbox_işaretlenen)
password=""
i=0
for i in checkbox_işaretlenen:
    password += random.choice(i)


password += ''.join(random.choices(kl, k=a))



st.write("Your password is:", password)

#portfolyomuza koyalım
