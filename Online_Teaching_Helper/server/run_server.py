# -*-coding:utf-8-*-

# 功能：服务器端，负责接受客户端请求，和DB交流
# 该数据库时这个老重点改，最后改数据库时用本子时刻备忘
# 需要加入教师端需要加入多线程来管理，放在后面实现

from flask import Flask
from do_with_DB.do_with_db import DB_opera
app = Flask(__name__)
db=DB_opera()

def listToDict(list):
    dict = {}
    for i, v in list:
        dict[str(i)] = v
    return dict

def listToDict_1(list):
    dict = {}
    index=1
    for i in list:
        dict[index]=i
        index+=1
    return dict

@app.route('/register/<id>/<passward>/<role>/<name>')
def register(id,passward,role,name):
    flag=db.register(id,passward,role,name)
    if flag:
        print("about server")
        return {'flag':True}
    return {'flag':False}

@app.route('/login/<id>/<passward>/<role>/')
def login(id,passward,role):
    flag =db.login_check(id,passward,role)
    if flag:
        return {"legal":True}
    return {"legal":False}

@app.route('/new_class/<class_id>/<class_name>/<teacher_id>')
def new_class(class_id,class_name,teacher_id):
    flag=db.new_class(class_id,class_name,teacher_id)
    print("server flag is",flag)
    if flag:
        return {"flag":True}
    return {"flag":False}

#开始课程
@app.route('/class/begin/<classID>')
def beginClass(classID):
    ok = db.begin_class(int(classID))
    return {'result': ok}

#根据课堂码，进入教室，此时和DB无交互，应该是线程管理器的事情
#要考虑的是，是更加课程编号进入线程，然后自动生成reID
#还是每次都要新的reID
# @app.route('/class/sign/<reportID>/<studentID>')
# def enterClass(reportID, studentID):
#     ok = db.sign_in_class(reportID, studentID)
#     return {'result': ok}

#在结束课堂后，应该关闭线程，同时在report中加一条数据
#那现在的参数不够，参加数据库，
#还有要存的数据，和生命周期有关
@app.route('/class/end/<reportID>/<studentID>/<grade>')
def endClass(reportID, studentID, grade):
    ok = db.end_class(reportID, studentID, grade)
    return {'result': ok}

#应该是线程管理器中的线程编号
@app.route('/sign/<reportID>')
def showSign(reportID):
    signs = db.show_sign_in(reportID)
    return dict(signs)

#从report里select Sid=ID
@app.route('/history/student/report/<studentID>')
def studentReportHistory(studentID):
    history = db.query_history_student(studentID)
    return dict(history)

#展示好想没用到，应该就是和s表交互
@app.route('/inform/student/<studentID>')
def studentInform(studentID):
    inform = db.show_inform_student(int(studentID))
    return listToDict_1(inform)

#同上
@app.route('/inform/teacher/<teacherID>')
def teacherInform(teacherID):
    inform = db.show_inform_teacher(teacherID)
    return listToDict_1(inform)

#花名册，从cs表里cid就行
@app.route('/namelist/<classID>')
def nameList(classID):
    nameList = db.check_namelist(classID)
    return listToDict_1(nameList)

#由班级号找report，那确实少了一个表--
#或者这样
#cid->rid 然后只显示cid,rid,date_和selet,并且只显示一条
#行得通
@app.route('/history/class/<class_id>')
def query_history_by_teacher(class_id):
    history = db.query_history_teacher(class_id)
    return dict(history)

#teaid-》c_id->rid
@app.route('/history/teacher/brief/<tearcherID>')
def show_brief_history_teacher(tearcherID):
    history = db.show_brief_history_teacher(tearcherID)
    return listToDict_1(history)

#直接在report里找到
@app.route('/history/student/brief/<studentID>')
def show_brief_history_student(studentID):
    history = db.show_brief_history_student(studentID)
    return listToDict_1(history)


if __name__ == "__main__":
    app.run(host='0.0.0.0')