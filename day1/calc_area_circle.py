# 1. คำนวณพื้นที่วงกลม calc_area_circle.py
# สูตรการหาพื้นที่วงกลม = พาย x รัศมี2

pi:float = 3.14159265359
input_num:float  = input("Enter radius: ")
print("input is " + input_num)
area_of_circle:float = pi * (float(input_num) * float(input_num))
print("Area of circle is " + str(area_of_circle))