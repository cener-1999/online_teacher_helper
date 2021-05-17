# -*-coding:utf-8-*-
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

@app.route('/class/begin/<classID>')
def beginClass(classID):
    ok = db.begin_class(int(classID))
    return {'result': ok}

@app.route('/class/sign/<reportID>/<studentID>')
def enterClass(reportID, studentID):
    ok = db.sign_in_class(reportID, studentID)
    return {'result': ok}

@app.route('/class/end/<reportID>/<studentID>/<grade>')
def endClass(reportID, studentID, grade):
    ok = db.end_class(reportID, studentID, grade)
    return {'result': ok}

@app.route('/sign/<reportID>')
def showSign(reportID):
    signs = db.show_sign_in(reportID)
    return dict(signs)

@app.route('/history/student/report/<studentID>')
def studentReportHistory(studentID):
    history = db.query_history_student(studentID)
    return dict(history)

@app.route('/inform/student/<studentID>')
def studentInform(studentID):
    inform = db.show_inform_student(int(studentID))
    return listToDict_1(inform)

@app.route('/inform/teacher/<teacherID>')
def teacherInform(teacherID):
    inform = db.show_inform_teacher(teacherID)
    return listToDict_1(inform)

@app.route('/namelist/<classID>')
def nameList(classID):
    nameList = db.check_namelist(classID)
    return listToDict_1(nameList)

@app.route('/history/class/<class_id>')
def query_history_by_teacher(class_id):
    history = db.query_history_teacher(class_id)
    return dict(history)

@app.route('/history/teacher/brief/<tearcherID>')
def show_brief_history_teacher(tearcherID):
    history = db.show_brief_history_teacher(tearcherID)
    return listToDict_1(history)

@app.route('/history/student/brief/<studentID>')
def show_brief_history_student(studentID):
    history = db.show_brief_history_student(studentID)
    return listToDict_1(history)


if __name__ == "__main__":
    app.run(host='0.0.0.0')