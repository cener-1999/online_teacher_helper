# -*-coding:utf-8-*-
# 功能：建数据库
# 备注：底下几个条代码去注释，只需要运行一遍
# 需要修改
#5.19 修改完成

import enum

import pymysql
from sqlalchemy import Column, Integer, String, Enum, create_engine, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import select
from do_with_DB.Session import get_session
from sqlalchemy.sql import func


engine = create_engine('mysql+pymysql://root:nbuser@localhost:3306/OTH?charset=utf8', echo=True)
# 声明映射
Base = declarative_base()
#映射声明，基类
Base = declarative_base()

session=get_session()

class RoleEnum(enum.Enum):
    teacher=1
    student=2

class MoodEnum(enum.Enum):
    angry=1
    disgust=2
    scared=3
    happy=4
    sad=5
    surprised=6
    neutral=7

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


class Class_Students(Base):
    __tablename__='Class_Students'
    index=Column(Integer,autoincrement=True,primary_key=True)
    Class_ID=Column(Integer,ForeignKey(Class.ClassID))
    StudentID=Column(Integer, ForeignKey(Student.ID))

class Reports(Base):
    __tablename__="Reports"
    ReportID=Column(Integer,autoincrement=True,primary_key=True)
    classID=Column(Integer,ForeignKey(Class.ClassID))
    StudentID=Column(Integer, ForeignKey(Student.ID))
    grade=Column(Integer,default=0)
    Select=Column(Enum(MoodEnum))
    Create_time = Column(DateTime,default=func.now())

#建表
Base.metadata.create_all(engine)
