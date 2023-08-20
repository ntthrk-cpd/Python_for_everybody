import streamlit as st
import random
# install with: pip install streamlit
# run with: streamlit run main.py
# ref: https://docs.streamlit.io/en/stable/api.html
''' 
สร้าง web app ได้ง่ายๆ โดยไม่ต้องเขียน html, css, javascript เอง แต่ต้องมี python ในการเขียน code แทน 
สามารถเขียนได้ง่ายๆ และเร็วกว่า แต่ไม่สามารถทำได้ทุกอย่าง และไม่สามารถ customize ได้มาก แต่สามารถเขียนเพื่อใช้งานได้ง่ายกว่า 

'''
# สร้างหัวข้อ
st.title("แดชบอร์ดของฉัน") # แสดงหัวข้อ
st.caption("อันนี้เอาไว้แสดงอะไรดี") # แสดงคำอธิบาย

age = st.text_input("อายุของคุณ", 20) # แสดงช่องให้กรอกข้อมูล และเก็บค่าที่กรอกไว้ในตัวแปร age
# height = st.text_input("ส่วนสูงของคุณ", 170) # แสดงช่องให้กรอกข้อมูล และเก็บค่าที่กรอกไว้ในตัวแปร height
height = st.slider("ส่วนสูงของคุณ (cm)", 100, 200, 170) # แสดง slider ให้เลื่อนเลือกค่า และเก็บค่าที่เลือกไว้ในตัวแปร height
# weight = st.text_input("น้ำหนักของคุณ", 70) # แสดงช่องให้กรอกข้อมูล และเก็บค่าที่กรอกไว้ในตัวแปร weight
weight = st.slider("น้ำหนักของคุณ (kg)", 40, 150, 70) # แสดง slider ให้เลื่อนเลือกค่า และเก็บค่าที่เลือกไว้ในตัวแปร weight
# weight = st.number_input("น้ำหนักของคุณ", 40, 150, 70) # แสดงช่องให้กรอกข้อมูล และเก็บค่าที่กรอกไว้ในตัวแปร weight

if (age and height and weight): # ถ้ามีข้อมูลทั้ง 3 ตัว
    bmi = float(weight) / ((float(height)/100)**2)
    st.write("ค่า BMI ของคุณคือ", bmi)

st.metric("อุณหภูมิในบ้าน", 35, 1) # แสดงตัวเลข และเปรียบเทียบกับค่าเดิม
st.metric("อุณหภูมินอกบ้าน", 35, -1) 

# เขียนบนหน้าจอ
st.write("Hello World") # write text to web page
v_dict = {"a": "b"}
v_num = random.randint(1, 10)
v_list = [1, 2, 3, 4, 5]
st.write(v_dict) # write dictionary to web page
st.write(v_num) # write number to web page
st.write(v_list) # write list to web page


