# -*-coding:utf-8-*-
# 提供数据库方法，与server搞定相关，修改时注意参数和返回值
# 需要修改

from sqlalchemy import func
from sqlalchemy.dialects.mysql import pymysql
from sqlalchemy.orm import DeclarativeMeta, session
from sqlalchemy.sql import exists
from sqlalchemy import Column, Integer, String, Enum, create_engine, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
from sqlalchemy.sql.expression import select
from do_with_DB.map import DbSharding
from do_with_DB.Session import get_session
from do_with_DB.createTable import Class_Students, User,Teacher,Student,RoleEnum,Class,Reports

engine = create_engine('mysql+pymysql://root:nbuser@localhost:3306/OTH?charset=utf8', echo=True)
'''数据库从删库到跑路'''
class DB_opera():
    def login_check(self,id,passward,role):#is ok
        session=get_session()
        id=int(id)
        passward=int(passward)
        legal= session.query(User).filter(User.ID ==id,User.pwsd==passward,User.Role==role).count()
        if legal ==1:
            print("ok")
            session.close()
            return True
        session.close()
        return False

    def register(self,id, passward, role, name):
        session = get_session()
        #print('if work?')
        id = int(id)
        passward=int(passward)
        name=str(name)
        legal = session.query(User).filter(User.ID == id).count()
        print('legal is',legal)
        if legal <1:
            user_obj = User(ID=id, pwsd=int(passward), Role=role)
            session.add(user_obj)
            session.commit()
            if (role == "teacher"):
                teacher_obj = Teacher(ID=id, name=name)
                session.add(teacher_obj)
                session.commit()
            else:
                student_obj = Student(ID=id, name=name, roomID=id + 1)
                session.add(student_obj)
                session.commit()
                session.close()
            return True
        session.close()
        return False

    # def begin_class(self,class_id):#beging a class
    #     session = get_session()
    #     reports_obj = Reports(classID=class_id)
    #     session.add(reports_obj)
    #     session.commit()
    #     """建表"""
    #     reportid=reports_obj.reportID#原来这样就可以获得新建项目的主键了吗
    #     print('newID is',reportid)
    #     create_report=Create.create_report(reportid)
    #     create_report.metadata.create_all(engine)
    #     session.close()
    #     return True

#新建课程，和Class交互，存老师id,课程id,课程名称
    def new_class(self,class_id, class_name, teacher_id):
        session = get_session()
        class_id=int(class_id)
        teacher_id=int(teacher_id)
        legal=session.query(Class).filter(Class.ClassID==class_id).count()
        print(legal)
        if legal<1:
            class_obj = Class(ClassID=class_id, Class_name=class_name, teacherID=teacher_id)
            session.add(class_obj)
            session.commit()
            session.close()
            return True
        #print("here?")
        session.close()
        return False

#不要dbmap
#和CS表交互，数据库没问题
#改方法
#修改完成，且通过测试
    def join_class(self,class_id,student_id):
        student_id=int(student_id)
        session=get_session()
        join_obj=Class_Students(Class_ID=class_id,StudentID=student_id)
        session.add(join_obj)
        try:
            session.commit()
        except :
            print('该学生已经在课堂内了')
        session.close()

#找老师教了什么课程，返回列表
    def find_teahcer_class(self,teacher_id):
        classlist=[]
        session=get_session()
        class_row=session.query(Class).filter(Class.teacherID==int(teacher_id))
        #寻找到多个结果，需要将其取出
        #for item in class_row:
            

    def sign_in_class(self,report_id,student_id):
        session=get_session()
        dbmap=DbSharding()
        report=dbmap.get_model(str(report_id))
        sign_obj=report(StudentID=int(student_id))
        session.add(sign_obj)
        session.commit()
        session.close()
        return True

    def end_class(self,report_id,student_id,grade_):
        session = get_session()
        dbmap = DbSharding()
        reportid = dbmap.get_model(str(report_id))
        update_row=session.query(reportid).filter(reportid.StudentID==int(student_id)).one()#!!!是这里 因为默认all()返回是一个队列
        if update_row:
            update_row.grade=int(grade_)
            session.add(update_row)
            session.commit()
        session.close()
        return True

    def show_sign_in(self,report_id):#test ok
        sign_in_list=[]
        session = get_session()
        dbmap = DbSharding()
        reportid = dbmap.get_model(str(report_id))
        list=session.query(reportid).all()
        for item in list:
            student_id=item.StudentID
            student=session.query(Student).filter(Student.ID==student_id).one()
            student_name=student.name
            sign_in_list.append((student_id,student_name))
        print(sign_in_list)
        session.close()
        return sign_in_list

    def query_history_student(self,student_id):#终于写好了 感觉写了好久 不太清醒了
        histroylist=[]
        session=get_session()
        all_report=session.query(Reports).all()#这是一个 行 的列表
        print("000000", all_report)
        dbmap=DbSharding()
        for report in all_report:
            report_id=report.reportID#命名还是要给自己提示
            #print("!!!!!!!!!",report_id)
            find_report=dbmap.get_model(str(report_id))
            #print(find_report)
            if not find_report:
                print("没有课")
            if find_report!=False:
                falg=session.query(find_report).filter(find_report.StudentID==student_id).all()#这个flag没有用
                #print("????",len(falg))
                print(falg,'how you work?')
                if falg:
                    result=session.query(find_report).filter(find_report.StudentID==student_id).one()
                    histroylist.append((report_id,result.grade))
            #print(histroylist)
        print(histroylist)
        session.close()
        return histroylist

    def query_history_teacher(self,class_id):
        result_list=[]
        session=get_session()
        report_list=session.query(Reports).filter(Reports.classID==int(class_id)).all()
        for report in report_list:
            result_list.append((report.reportID,class_id))
        session.close()
        print(result_list)
        return result_list#

    def check_namelist(self,class_id):
        namelist=[]
        session=get_session()
        namelist_=session.query(Class_Students).filter(Class_Students.Class_ID==class_id)
        for student in namelist_:
            student_id=student.StudentID
            studentname_=session.query(Student).filter(Student.ID==student_id).one()
            studentname=studentname_.name
            namelist.append((student_id,studentname))
        print(namelist)
        session.close()
        return namelist

        # dbmap=DbSharding()
        # theclass=dbmap.get_model(str(class_id))
        # row_name_list=session.query(theclass).all()
        # for item in row_name_list:
        #     student_id=item.StudentID
        #     student=session.query(Student).filter(Student.ID==student_id).all()
        #     for item in student:
        #         student_name=item.name
        #         namelist.append((student_id,student_name))
        # print(namelist)
        # session.close()
        # return namelist

    def show_inform_teacher(self,teacher_id):
        list = []
        session=get_session()
        teachers_classes=session.query(Class).filter(Class.teacherID==int(teacher_id)).all()
        for item in teachers_classes:
            #第一个theclass是表的一列，下一行的class_name是从那一列中取出属性
            class_name=item.Class_name
            sum_=session.query(Class_Students).filter(Class_Students.Class_ID==item.ClassID).count()
            class_id=item.ClassID
            list.append((class_id,class_name,sum_))
        print(list)
        session.close()
        return list
        # list = []
        # session=get_session()
        # dbmap=DbSharding()
        # result_list=session.query(Class).filter(Class.teacherID==int(teacher_id)).all()
        # for item in result_list:
        #     class_id=item.ClassID
        #     class_name=item.Class_name
        #     findlist=dbmap.get_model(str(class_id))
        #     sum=session.query(findlist).count()
        #     list.append((class_id,class_name,sum))
        # print(list)
        # session.close()
        # return list

    def show_brief_history_teacher(self,teacher_id):#md 意外的顺利啊
                #找到reports表里的所有reportid，按名字找到表，如果表里有studentid，加入元组
        list = []
        session = get_session()
        teachers_classes=session.query(Class).filter(Class.teacherID==int(teacher_id)).all()
        for item in teachers_classes:
            class_id=item.ClassID
            class_name=item.Class_name
            reports=session.query(Reports).filter(Reports.classID==item.ClassID).all()
            for report in reports:
                report_id=report.ReportID
                list.append((class_id, class_name, report_id))

        print(list)  
        return list  
        # list = []
        # session = get_session()
        # dbmap = DbSharding()
        # result_list = session.query(Class).filter(Class.teacherID == int(teacher_id)).all()
        # for item in result_list:
        #     class_id = item.ClassID
        #     class_name = item.Class_name
        #     report_list=session.query(Reports).filter(Reports.classID==int(class_id)).all()
        #     for i in report_list:
        #         list.append((class_id,class_name,i.reportID))
        # print(list)
        # session.close()
        # return list

    def show_inform_student(self,student_id):
        list = []
        session=get_session()
        students_classes=session.query(Class_Students).filter(Class_Students.StudentID==int(student_id)).all()
        for item in students_classes:
            #第一个theclass是表的一列，下一行的class_name是从那一列中取出属性
            theclass=session.query(Class).filter(Class.ClassID==item.Class_ID).one()
            class_name=theclass.Class_name

            theteacher1=session.query(Class).filter(Class.ClassID==item.Class_ID).one()
            theteacher2=session.query(Teacher).filter(Teacher.ID==theteacher1.teacherID).one()
            teacher_name=theteacher2.name
            class_id=item.Class_ID

            list.append((class_id,class_name,teacher_name))
        print(list)
        session.close()
        return list
            
        # for item in all_class_list:
        #     class_id=item.ClassID
        #     i=dbmap.get_model(str(class_id))  #一个课程
        #     if i:
        #         n=session.query(i).filter(i.StudentID==student_id).all()
        #         #如果课程表上有自己
        #         if n:
        #             the_class=session.query(Class).filter(Class.ClassID==int(class_id)).one()
        #             class_name=the_class.Class_name
        #             teacher=session.query(Teacher).filter(Teacher.ID==the_class.teacherID).one()
        #             teacher_name=teacher.name
        #             list.append((class_id,class_name,teacher_name))
        # print(list)
        # session.close()
        # return list

    def show_brief_history_student(self,student_id):
        #找到reports表里的所有reportid，按名字找到表，如果表里有studentid，加入元组
        list = []
        session = get_session()
        student_reports=session.query(Reports).filter(Reports.StudentID==student_id).all()
        for report in student_reports:  
            class_id=report.classID
            mygrade=report.grade

            theclass=session.query(Class).filter(Class.ClassID==report.classID).one()
            class_name=theclass.Class_name

            list.append((class_id, class_name, mygrade))
        print(list)  
        return list  

        # dbmap = DbSharding()
        # all_report_list = session.query(Reports).all()
        # for item in all_report_list:
        #     report_id = item.reportID
        #     i = dbmap.get_model(str(report_id))  # 一个课程
        #     if i:
        #         n = session.query(i).filter(i.StudentID == student_id).all()
        #         # 如果课程表上有自己
        #         if n:
        #             myreport=session.query(i).filter(i.StudentID == student_id).one()
        #             mygrade=myreport.grade
        #             myclass=session.query(Reports).filter(Reports.reportID==int(report_id)).one()
        #             class_id=myclass.classID
        #             find_class_name=session.query(Class).filter(Class.ClassID==class_id).one()
        #             class_name = find_class_name.Class_name
        #             list.append((class_id, class_name, mygrade))
        # print(list)
        # session.close()
        # return list


#new_class(1001,"english",222)
#new_class(1003,"CS",222)
#new_reports(1000)
#new_report(1000,101,99)


#test=DB_opera()
#test.register(102,121,"student","zhangsan")
#test.login_check(101,154,"student")
#test.find_teahcer_class(987)
# test.new_class(101,"OOAD",110001)
# test.new_class(102,"CS",110001)
# test.new_class(103,"OS",110001)
# test.begin_class(101)
# test.begin_class(102)
# test.begin_class(103)
#test.begin_class(500)
#test.sign_in_class(1020,147)
# test.end_class(6,2020100001,80)
# test.end_class(5,2020100001,90)
# test.end_class(4,2020100001,65)
#test.begin_class(500)
#test.sign_in_class(1009,101)
#test.show_sign_in(1018)
#test.query_history_student(147)
#test.query_history_teacher(500)
#test.check_namelist(453)
#test.show_inform_teacher(987)
#test.show_brief_history_teacher(987)
#test.show_inform_student(2020100001)
#test.show_brief_history_student(101)
#test.begin_class(1344)
# test.join_class(101,2020100001)
# test.join_class(102,2020100001)
# test.join_class(103,2020100001)
# test.sign_in_class(4,2020100002)
# test.sign_in_class(6,2020100002)
"""" 从1000初始化
session=get_session()
reports_obj = Reports(reportID=1000,classID=1000)
session.add(reports_obj)
session.commit()
"""
'''
session = get_session()
user_obj = User(ID=101, pwsd=154, Role=RoleEnum.student)
student_obj = Student(ID=101, name="zhangsan", roomID=101)
session.add(user_obj)
session.commit()
session.add(student_obj)
session.commit()
'''
'''
session = get_session()
report_obj=Class(ClassID=1000,Class_name='math',teacherID=222)
session.add(report_obj)
session.commit()
'''


#register(1111,5555,"teacher","name1")