

def picked_teacher():
    lessons_dict={}
    num_students=int(input("number of students"))
    #function that gets num of students from input
    for i in range(num_students):
        student_name=input("student_name")
        #screen input

        subject_for_tutoring=input("subject for tutoring")
        #screen function

        students_grade=input("students_grade")
        #screen input

        lessons_dict.update({student_name:(subject_for_tutoring,students_grade)})
        print(lessons_dict)
picked_teacher()