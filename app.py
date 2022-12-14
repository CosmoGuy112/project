from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/result", methods=['POST'])
def output():
    if request.method == 'POST':
        student_list = request.form.get('student_list').split() #รหัสนักศึกษาของนักเรียนโดยจะให้ขึ้นต้นด้วย02
        teacher_list = request.form.get('teacher_list').split() #รหัสอาจารย์โดยจะให้ขึ้นต้นด้วย01
        numofclass = len(student_list)+ len(teacher_list)
        fan, light, air = 0, 0, 0 #เก็บค่าเป็น 0 ไว้ก่อนเพราะตอนแรกยังไม่มีการเปิดใช้งาน
        #เข้าเงื่อนไขการเปิด/ปิดไฟ พัดลมและแอร์ ต่อจำนวนคนในห้อง
        if numofclass <= 5 and numofclass > 0:
            fan += 1
            light += 1
            lessfive = ("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
        elif numofclass <= 10 and numofclass > 5:
            fan += 2
            light += 2
            lessfive = ("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
        elif numofclass <= 15 and numofclass > 10:
            fan += 3
            light += 3
            lessfive = ("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
        elif numofclass <= 20 and numofclass > 15:
            fan += 4
            light += 4
            lessfive = ("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
        elif numofclass <= 25 and numofclass > 20:
            air += 1
            light += 5
            lessfive = ("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
        elif numofclass <= 31 and numofclass > 25:
            air += 2
            light += 6
            lessfive = ("Fan : %d\nLight : %d\nAir : %d" %(fan, light, air))
        studenn = list(map(int,student_list)) #แสดงรหัสนักเรียนที่ขาดเรียน
        studennza = (studenn)
        set_one = set()
        set_two = set()
        set_three = set()
        set_ma = set()
        for i in range(20001,20011):
            set_one.add(i)
        for p in range(20011,20021):
            set_two.add(p)
        for p in range(20021,20031):
            set_three.add(p)
        for j in studennza:
            set_ma.add(j)
        ans_one = set_one.difference(set_ma)
        ans_two = set_two.difference(set_ma)
        ans_three = set_three.difference(set_ma)
        return render_template("result.html", fan_light=lessfive, missing_one=ans_one, missing_two=ans_two, missing_three=ans_three, data=True)
        

if __name__ == "__main__":
    app.run(debug=True)
