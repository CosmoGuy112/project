""" KMITL PROJECT """
def numclass():
    """ SMARTCLASSROOM """
    student_list = [] #รหัสนักศึกษาของนักเรียนโดยจะให้ขึ้นต้นด้วย02
    teacher_list = [] #รหัสอาจารย์โดยจะให้ขึ้นต้นด้วย01
    while True:
        id_num = input() #อินพุตรหัสนักศึกษาและรหัสอาจารย์เท่านั้น
        if id_num[:2] == '00':
            break
        if id_num[:2] == '01':
            teacher_list.append(id_num)
        elif id_num[:2] == '02':
            student_list.append(id_num)
        numofclass = len(student_list)+len(teacher_list)
    print(sorted(student_list))
numclass()
def fan():
    fan, light, air = 0, 0, 0
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
fan()
    
#     all_people = ['020001', '020002', '020003', '020004', '020005', '020006'\
#     '020007', '020008', '020009', '020010', '020011', '020012', '020013', '020014', '020015'\
#     '020016', '020017', '020018', '020019', '020020', '020021', '020022', '020023', '020024'\
#     '020025', '020026', '020027', '020028', '020029', '020030']
#     for _ in range(30):
#         all_people.remove(id_num)
#     all_people = ''.join(all_people)
#     print(all_people)
















