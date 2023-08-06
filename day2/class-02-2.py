age = 4
is_arg_more_than_5: bool = age > 5

# if statement
if age > 5:
    print("You can use the slide") # ถ้าเงื่อนไขเป็นจริงจะทำงานที่อยู่ในเงื่อนไขนี้ ถ้าเป็นเท็จจะข้ามไปไม่ทำงาน และทำงานต่อที่บรรทัดถัดไป หรือเงื่อนไขถัดไป (ถ้ามี)  
elif age <= 3:
    print("You can't use the slide")
else:
    print("You can use the slide with your parents")