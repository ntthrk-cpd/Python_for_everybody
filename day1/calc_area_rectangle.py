# 2. คำนวณพื้นที่สี่เหลี่ยม calc_area_rectangle.py

# สูตรการหาพื้นที่สี่เหลี่ยมผืนผ้า = กว้าง x ยาว
size_of_sides_wide:float  = input("Enter size of sides (cm): ")
print("size input_wide is " + size_of_sides_wide )
size_of_sides_long:float  = input("Enter size of sides (cm): ")
print("size input_long " + size_of_sides_long )
area_of_rectangle:float = float(size_of_sides_wide) * float(size_of_sides_long)
print("Area of rectangle is " + str(area_of_rectangle))

# # สูตรการหาพื้นที่สี่เหลี่ยมจัตุรัส = ด้าน x ด้าน 
# size_of_sides_sq:float  = input("Enter size of sides: ")
# print("size input is " + size_of_sides_sq )
# area_of_square:float = float(size_of_sides_sq) * float(size_of_sides_sq)
# print("Area of square is " + str(area_of_square))


