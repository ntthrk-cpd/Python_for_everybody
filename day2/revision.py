# Calculate area of a circle

PI = 3.141592653589793 # ค่าคงที่ไม่ต้องเปลี่ยนแปลง ใช้ตัวพิมพ์ใหญ่เสมอ และใช้ _ แทนช่องว่าง

radius: str = input("Enter radius: ") # มี type เป็น  str เสมอ จะต้องเปลี่ยนเป็นค่าที่ใช้ก่อนคำนวณ
radius = float(radius) # แปลงเป็น float ก่อนคำนวณ
area: float = PI * radius ** 2 # คำนวณพื้นที่ และเก็บไว้ในตัวแปร area
print("Area of circle: " , area) # print สามารถรับ ค่า (object) ได้หลายค่า โดยใช้ , คั่น
