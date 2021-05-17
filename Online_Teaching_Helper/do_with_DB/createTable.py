# -*-coding:utf-8-*-
# 功能：建数据库
# 备注：底下几个条代码去注释，只需要运行一遍
# 需要修改

import enum

import pymysql
from sqlalchemy import Column, Integer, String, Enum, create_engine, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from do_with_DB.Session import get_session
from sqlalchemy.sql import func

engine = create_engine('mysql+pymysql://root:nbuser@localhost:3306/online_teaching_helper?charset=utf8', echo=True)
# 声明映射
Base = declarative_base()
#映射声明，基类
Base = declarative_base()

session=get_session()

class RoleEnum(enum.Enum):
    teacher=1
    student=2

class User(Base):
    __tablename__='USER'
    ID=Column(Integer,primary_key=True)
    pwsd=Column(Integer)
    Role=Column(Enum(RoleEnum))

    def __repr__(self):
        ID = self.ID
        passward = self.pwsd
        Role = self.Role
        return f"Course:(ID={ID},ROLE={Role})"

class Teacher(Base):
    __tablename__="Teacher"
    ID=Column(Integer,ForeignKey(User.ID),primary_key=True)
    name=Column(String(100))

class Student(Base):
    __tablename__="Student"
    ID=Column(Integer,ForeignKey(User.ID),primary_key=True)
    name=Column(String(100))
    roomID=Column(Integer)

class Class(Base):
    __tablename__='Class'
    ClassID=Column(Integer,primary_key=True)
    Class_name=Column(String(30))
    teacherID=Column(Integer,ForeignKey(Teacher.ID))

class ClassList(Base):
    __tablename__ = 'ClassList'
    ClassID = Column(Integer, ForeignKey(Class.ClassID),primary_key=True)
    StudentID = Column(Integer, ForeignKey(Student.ID))

class Reports(Base):
    __tablename__="Reports"
    reportID=Column(Integer,autoincrement=True,primary_key=True)
    classID=Column(Integer,ForeignKey(Class.ClassID))
    create_time = Column(DateTime,default=func.now())

class Create():
    #建立课程花名册的函数
    def create_class_list(self,class_id):
        Model = declarative_base()  # 生成一个SQLORM基类
        class CreateClassList(Model):
            __tablename__ = str(class_id)
            StudentID=Column(Integer,ForeignKey(Student.ID),primary_key=True)
        return CreateClassList

    def create_report(self,report_id):
        Model = declarative_base()  # 生成一个SQLORM基类
        class CreateReport(Model):
            __tablename__ = str(report_id)
            StudentID=Column(Integer,ForeignKey(Student.ID),primary_key=True)
            grade=Column(Integer,default=None)
        return CreateReport

# create=Create()
# create.create_class_list(101).metadata.create_all(engine)
# create.create_class_list(102).metadata.create_all(engine)
# create.create_class_list(103).metadata.create_all(engine)
Base.metadata.create_all(engine)

