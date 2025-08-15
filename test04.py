# กรณี 1 print() มีข้อมูลกลายประเภททำไง? มี 4 วิธี
# วิธี 1 
print("hello",555,"wow",999,True,10 + 100)

# วิธี 2 + ต้องทำให้เป็น string
# ไม่เว้น 1 space 
print("hello" + str(555) + "wow" + str(True)) 
print("hello " + str(555) +  " wow " + str(True)) 

# วิธี 3 ใช้เมธอด format
# (ข้อมูลที่ไม่ใช้ string ให้ใส่ใน () ของ format และตำแหล่งที่แสดงข้อมูลนั้นใส่ {} แทน)
print("hello {} wow {} {} hi {} {}".format(555,999,True,10+20,15.22))
# index number 0 1 2 
print("{2} {0}".format("a","b","c"))

# วิธี 4 f-string โดยข้อมูลที่แสดงอยู่ในรูปแบบของ string โดยมี f อยู่ข้างหน้า
# (ข้อมูลที่ไม่ใช้ string ใส่ใน {} แทน)
print(f"hello {555} wow {True} {10+10} {15.22}")