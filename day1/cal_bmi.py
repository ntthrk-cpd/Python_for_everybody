# 3.คำนวณ BMI cal_bmi.py
# สูตรการหาค่า BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)

weight:float  = input("Enter weight (kg): ")
print("weight is " + weight)
height:float  = input("Enter height (m): ")
print("height is " + height)
bmi:float = float(weight) / float(height) ** 2
print("BMI is " + str(bmi))