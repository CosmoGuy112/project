""" KMITL PROJECT """
def numclass():
    """ SMARTCLASSROOM """
    student_list = [] #รหัสนักศึกษาของนักเรียนโดยจะให้ขึ้นต้นด้วย20
    teacher_list = [] #รหัสอาจารย์โดยจะให้ขึ้นต้นด้วย10
    while True:
        id_num = input() #อินพุตรหัสนักศึกษาและรหัสอาจารย์เท่านั้น
        if id_num[:2] == '00':
            break
        if id_num[:2] == '10':
            teacher_list.append(id_num)
        elif id_num[:2] == '20':
            student_list.append(id_num)
        numofclass = len(student_list)+len(teacher_list)

    fan, light, air = 0, 0, 0 #เก็บค่าเป็น 0 ไว้ก่อนเพราะตอนแรกยังไม่มีการเปิดใช้งาน
    #เข้าเงื่อนไขการเปิด/ปิดไฟ พัดลมและแอร์ ต่อจำนวนคนในห้อง
    if numofclass <= 5 and numofclass > 0:
        fan += 1
        light += 1
        print("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
    elif numofclass <= 10 and numofclass > 5:
        fan += 2
        light += 2
        print("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
    elif numofclass <= 15 and numofclass > 10:
        fan += 3
        light += 3
        print("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
    elif numofclass <= 20 and numofclass > 15:
        fan += 4
        light += 4
        print("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
    elif numofclass <= 25 and numofclass > 20:
        air += 1
        light += 5
        print("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
    elif numofclass <= 31 and numofclass > 25:
        air += 2
        light += 6
        print("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
        
    studenn = list(map(int,student_list)) #แสดงรหัสนักเรียนที่ขาดเรียน
    studennza = (studenn)
    set_all = set()
    set_ma = set()
    for i in range(20001,20031):
        set_all.add(i)
    for j in studennza:
        set_ma.add(j)
    ans = set_all.difference(set_ma)
    print("นักเรียนที่ขาดเรียน :" ,*ans)
    
numclass()















