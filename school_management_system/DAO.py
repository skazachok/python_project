from Models import Student
from Models import Course
from Models import Attending

class StudentDAO:
    def __init__(self):
        self.__student_list=[]
        with open("students.csv", mode = 'r+') as st:
            for line in st.read()[:-1].split("\n"):
                email, s_name, s_password = line.split(',')
                
                s=Student(email,s_name,s_password)
                self.__student_list.append(s)
        
    def get_students(self):
        return self.__student_list
    
    def validate_user(self, email, pw):
        #sl=self.get_students()
        for i in self.__student_list:
            #print(i.email, email, i.password, pw)
            if i.email == email and i.password == pw:
                return True
        return False
    
    def get_student_by_email(self, email):
        for i in self.__student_list:
            if i.email == email:
                return i
    
class CourseDAO:
    def __init__(self):
        self.__courses_list=[]
        
        with open("courses.csv", mode = 'r+') as co:
            for line in co.read()[:-1].split("\n"):
                id_c, name, instructor=line.split(',')
                
                c=Course(id_c,name,instructor)
                self.__courses_list.append(c)

    def get_courses(self):
        return self.__courses_list
    
class AttendingDAO:
    def __init__(self):
        self.__attending_list=[]
    
        with open("attending.csv", mode = 'r+') as at:
            for line in at.read()[:-1].split("\n"):
            #for line in at.read().split("\n"):
                c_id, st_email=line.split(',')
                
                a=Attending(c_id, st_email)
                self.__attending_list.append(a)

        
    def get_attending(self):
        return self.__attending_list
    
    def get_student_courses(self, course_list, email):
        lc=[]
        for i in course_list:
            for j in self.__attending_list:
                if i.c_id == j.course_id and email == j.student_email:
                    lc.append(i)
        return lc
        
    def register_student_to_course(self, email, course_id, course_list):
        #check if the course_id is in the course list
        exist=False
        for i in course_list:
            if i.c_id == course_id:
                exist=True
                break

        if exist:
            for i in self.__attending_list:
                if i.course_id == course_id and i.student_email == email:
                    print("You are already registered in the course {}".format(course_id))
                    exist=False

            a=Attending(course_id, email)
            self.__attending_list.append(a)
            self.save_attending()
        else:
            print("\nInvalid course {}. Please, enter a valid course id".format(course_id))
            return False
        return exist
        
    def save_attending(self):
        with open("attending.csv", mode = 'w') as at:
            for i in self.__attending_list:
                at.write(i.course_id + ',' + i.student_email + '\n')

