import sqlite3
connection = sqlite3.connect("AdaptiveLearining.db")

class Teacher:
    cursor = connection.cursor()
    def __init__(self):

        format_str="""CREATE TABLE IF NOT EXISTS course 
                            (   Course_ID INTEGER PRIMARY KEY,
                                Course_Name TEXT NOT NULL
                            );"""
        Teacher.cursor.execute(format_str)
        connection.commit()
        format_str="""CREATE TABLE IF NOT EXISTS quiz 
                            (   Quiz_No INTEGER PRIMARY KEY AUTOINCREMENT,
                                Course_ID INTEGER,
                                status CHAR(1) NOT NULL,
                                FOREIGN KEY (Course_Id) REFERENCES course(Course_ID) ON UPDATE CASCADE
                                ON DELETE CASCADE
                            );"""
        Teacher.cursor.execute(format_str)
        connection.commit()

    def helper(self,id):
        format_str="""CREATE TABLE IF NOT EXISTS "{course_id}"
                            (   Question_no INTEGER PRIMARY KEY AUTOINCREMENT,
                                Question Char(100) NOT NULL,
                                option1 Char(20) NOT NULL,
                                option2 Char(20) NOT NULL,
                                option3 Char(20) NOT NULL,
                                option4 Char(20) NOT NULL,
                                answers Char(20) NOT NULL
                            );"""
        self.sql_command = format_str.format(course_id=id)
        Teacher.cursor.execute(self.sql_command)
        connection.commit()
        self.__check=True
        while(self.__check):
            print("If You want add Another question Press Y else N")
            self.__temp_check=str(input())
            if self.__temp_check=='N':
                self.__check=False
            else:
                print("Enter the Question and Four options and correct answers")
                print("--Please add correct options Numbers seperated by comma if there are Multiple Correct Answers--")
                self.__qlist=[]
                for _ in range(6):
                    self.__tempq=str(input())
                    self.__qlist.append(self.__tempq)
                format_str = """INSERT INTO "{quiz_id}" 
                                (   Question, 
                                    option1,
                                    option2,
                                    option3,
                                    option4,
                                    answers
                                ) VALUES ("{q}","{a}", "{b}","{c}","{d}","{ans}");"""
                self.sql_command = format_str.format(   quiz_id=id,
                                                        q=self.__qlist[0],
                                                        a=self.__qlist[1],
                                                        b=self.__qlist[2],
                                                        c=self.__qlist[3],
                                                        d=self.__qlist[4],
                                                        ans=self.__qlist[5]
                                                    )
                Teacher.cursor.execute(self.sql_command)
                connection.commit()
                
    def add_quiz(self):
        self.show_table("course")
        self.show_table("quiz")
        print("Enter the Course ID for which you want to add quiz: ")
        self.__temp=int(input())
        format_str="""UPDATE quiz SET status = "Y" WHERE course_id = {course_id};"""
        self.sql_command = format_str.format(course_id=self.__temp)
        Teacher.cursor.execute(self.sql_command)
        connection.commit()
        self.helper(self.__temp)
        
    def delete_quiz(self,table_name=None):
        if(table_name==None):
            print("Select the Quiz table you want to delete")
            self.show_table("quiz")
            table_name=int(input())
        format_str="""DROP TABLE "{tb_name}";"""
        self.sql_command = format_str.format(tb_name=table_name)
        Teacher.cursor.execute(self.sql_command)
        
    def show_table(self,table_name=None):
        if(table_name==None):
            print("Please pass the table name as an argument ")
            return
        format_str="""SELECT * FROM "{tb_name}";"""
        self.sql_command = format_str.format(tb_name=table_name)
        Teacher.cursor.execute(self.sql_command)
        rows = Teacher.cursor.fetchall()
        for row in rows:
            print(row)

    def add_course(self):
        format_str="""SELECT * FROM COURSE;"""
        Teacher.cursor.execute(format_str)
        format_str = """INSERT INTO course (Course_ID, Course_Name) VALUES ("{course_id}", "{course_name}");"""
        print('Enter Course Id: ')
        self.__course_id=int(input())
        print('Enter Course Name: ')
        self.__course_name=str(input()).capitalize()

        self.sql_command = format_str.format(course_id=self.__course_id, course_name=self.__course_name)
        Teacher.cursor.execute(self.sql_command)
        connection.commit()

    def delete_course(self):
        format_str="""SELECT * FROM COURSE;"""
        Teacher.cursor.execute(format_str)
        print("Enter column name on which  you want to delete course i.e. Id or Name")
        self.__temp1=str(input())
        if self.__temp1=='id' or self.__temp1=='ID' or self.__temp1=='Id':
            print('Enter the Course Id you want to delete: ')
            self.__temp_id=int(input())
            format_str = """DELETE from course where Course_id={course_id};"""
            self.sql_command = format_str.format(course_id=self.__temp_id)
            Teacher.cursor.execute(self.sql_command)
            connection.commit()

        elif self.__temp1=='Name' or self.__temp1=='name' or self.__temp1=='NAME':
            print('Enter the Course Id you want to delete: ')
            self.__temp_cname=str(input())
            format_str = """DELETE from course where Course_Name="{course_name}";"""
            self.sql_command = format_str.format(course_name=self.__temp_cname)
            Teacher.cursor.execute(self.sql_command)
            connection.commit()

        else:
            print("------------Wrong Entry------------")
            print("------------ Try Agian ------------")

    def edit_course(self):
        format_str="""SELECT * FROM COURSE;"""
        Teacher.cursor.execute(format_str)
        print("Enter column name on which  you want to edit course i.e. Id or Name")
        self.__temp1=str(input())
        if self.__temp1=='id' or self.__temp1=='ID' or self.__temp1=='Id':
            print('Enter the Course Id you want to edit: ')
            self.__temp_id=int(input())
            print('Enter the course Id which you want to edit: ')
            self.__new_temp_id=int(input())
            format_str="""UPDATE course SET course_id = {new_id} WHERE course_id = {old_id};"""
            self.sql_command=format_str.format(new_id=self.__new_temp_id,old_id=self.__temp_id)
            Teacher.cursor.execute(self.sql_command)
            connection.commit()

        elif self.__temp1=='Name' or self.__temp1=='name' or self.__temp1=='NAME':
            print('Enter the Course Id you want to edit: ')
            self.__temp_cname=str(input())
            print('Enter the Course Id you which you want to edit: ')
            self.__new_temp_cname=str(input())
            format_str="""UPDATE course SET course_name = "{new_name}" WHERE course_name = "{old_name}";"""
            self.sql_command=format_str.format(new_name=self.__new_temp_cname,old_name=self.__temp_cname)
            Teacher.cursor.execute(self.sql_command)
            connection.commit()

        else:
            print("------------Wrong Entry------------")
            print("------------ Try Agian ------------")