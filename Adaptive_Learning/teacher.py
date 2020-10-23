import sqlite3
connection = sqlite3.connect("navigus.db")

class Teacher:
    cursor = connection.cursor()
    def __init__(self):

        
        #format_str="""create database if not exists `navigus`;"""
        #cursor.execute(format_str)
        format_str="""CREATE TABLE IF NOT EXISTS course 
                            (   Course_ID INTEGER PRIMARY KEY,
                                Course_Name TEXT NOT NULL
                            );"""
        Teacher.cursor.execute(format_str)
        connection.commit()

    def show_table(self):
        format_str="""SELECT * FROM COURSE;"""
        Teacher.cursor.execute(format_str)
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