from do_with_DB import do_with_db

class Test():
    def __init__(self) -> None:
        self.db_opera=do_with_db.DB_opera()

    def if_can_register(self,id,passward,role,name):
        self.db_opera.register(id, passward, role,name)

    def if_can_new_class(self,class_id, class_name, teacher_id):
        self.db_opera.new_class(class_id, class_name, teacher_id)

    def if_can_join_class(self,class_id,student_id):
        self.db_opera.join_class(class_id,student_id)

    def if_can_get_student_infor(self,student_id):
        self.db_opera.show_inform_student(student_id)

    def if_can_show_brief_student_report(self,student_id):
        self.db_opera.show_brief_history_student(student_id)

    # def if_can_new_class(self):
    #     self.db_opera.new_class()

#第一次测试，通过
test1=Test()
# test1.if_can_join_class(1, 2021000001)
# test1.if_can_register(100003,654321,"teacher","张三丰")
# test1.if_can_new_class(2,"太极拳法",100003)

#第二次测试，读取信息
#发现问题，CS表会重复，防止重复应该需要触发器检查，但是算了
test2=Test()
#test2.if_can_get_student_infor(2021000001)
test2.if_can_show_brief_student_report(2021000001)