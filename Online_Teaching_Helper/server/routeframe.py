# helper函数：将list转为dict
def listToDict(list):
    dict = {}
    for i, v in list:
        dict[str(i)] = v
    return dict

@app.route('/class/begin/<classID>')
def beginClass(classID):
    # ok = newreport(classID)
    # result =  True if ok else False
    # return {'result': result}
    pass

@app.route('/class/enter/<classID>/<studentID>')
def enterClass(classID, studentID):
    # ok = newclass(classID, studentID)
    # result =  True if ok else False
    # return {'result': result}
    pass

@app.route('/sign/<reportID>')
def showSign(reportID):
    # history = getHistory(studentID)
    # return dict(history)
    pass

@app.route('/class/end/<reportID>/<studentID>/<grade>')
def endClass(reportID, studentID, grade):
    # ok = new...(reportID, studentID, grade)
    # result =  True if ok else False
    # return {'result': result}
    pass

@app.route('/history/student/report/<studentID>')
def studentReportHistory(studentID):
    # history = getHistory(studentID)
    # return dict(history)
    pass

@app.route('/history/student/class/<studentID>')
def studentClassHistory(studentID):
    # history = getHistory(studentID)
    # return dict(history)
    pass

@app.route('/history/teacher/students/<tearcherID>')
def teacherStudentsHistory(tearcherID):
    # history = getHistory(tearcherID)
    # return dict(history)
    pass

@app.route('/history/teacher/classes/<teacherID>')
def teacherClassesHistory(teacherID):
    # history = getHistory(teacherID)
    # return dict(history)
    pass


@app.route('/namelist/<calssID>')
def nameList(classID):
    # nameList = getNameList(classID)
    # return dict(nameList)
    pass

@app.route('/inform/teacher/<teacherID>')
def teacherInform(teacherID):
    # inform = getInform(teacher)
    # return dict(inform)
    pass

@app.route('/inform/student/<studentID>')
def studentInform(studentID):
    # inform = getInform(teacher)
    # return dict(inform)
    pass
