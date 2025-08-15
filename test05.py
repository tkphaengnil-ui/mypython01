# คำสั่งรับค่าข้อความ string เป็นแป้นพิมพ์ input()
# * ตัวแปร variable คือ ชื่อที่ dev ตั้งขึ้นมาเอง (ต้องเป็นไปตามกฏการตั้งชื้อ) เอาไว้เก็บข้อมูล
# แปลงข้อความเป็นตัวเลข
fullname = input("ชื่อ: ")
year_born = input("ปีเกิด พ.ศ.: ")
print("--------------------")
print(f"สวัสดี {fullname}")
print(f"คุณเกิดในปี {year_born} ตอนนี้อายุ {2568 - int(year_born)}ปี")
print("--------------------")
print("สวัสดี", fullname)
print("คุณเกิดในปี", year_born , "ตอนนี้อายุ", 2568 - int(year_born),"ปี")
print("--------------------")
print("สวัสดี " + str(fullname))
print("คุณเกิดในปี " + str(year_born) + " ตอนนี้อายุ " + str(2568 - int(year_born)) + " ปี ")
# ยอมแพ้ครับ
print("--------------------")
print("สวัสดี {}".format(fullname))
print("คุณเกิดในปี {} ตอนนี้อายุ {} ปี".format(year_born, 2568 - int(year_born)))