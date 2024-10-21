import streamlit as s
s.title("Result Calculator")
p=s.number_input("enter your physics's marks")
m=s.number_input("enter your math's marks")
c=s.number_input("enter your chemistry's marks")

if p>33 and m>33 and c>33:
    s.write("pass")
else:
    s.write("fail")
