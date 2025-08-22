# สร้างโปรแกรมรับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้
# และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามา
# เป็นเท่าใด แล้วแสดงผลทางหน้าจอ
# สูตร  
# ผลรวม = เลขตัวที่1 + เลขตัวที่2 + เลขตัวที่3 + เลขตัวที่4 + เลขตัวที่5
# ค่าเฉลี่ย = ผลรวมของเลข 5 จำนวน / 5
 
# ============================
# Program  Average  5  Number
# ============================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
print('Program  Average  5  Number')

number1 =input('number 1 is : ')
number2 =input('number 2 is : ')
number3 =input('number 3 is : ')
number4 =input('number 4 is : ')
number5 =input('number 5 is : ')
num1 = int(number1) 
num2 = int(number2) 
num3 = int(number3) 
num4 = int(number4) 
num5 = int(number5)
sum = float(num1 + num2 + num3 + num4 + num5) 
aver = (int(sum) / 5)
print('Sum of 5 number is :', sum )
print('Average of 5 number is :', aver )