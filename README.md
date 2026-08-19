# hakaton---project


def matching_student_to_tutor(dict_of_all_students, list_all_tutors):
    list_outputs = []
    found_matching_tutor = False
    for student in dict_of_all_students:
        subject_student = dict_of_all_students[student][0]
        grade_student = dict_of_all_students[student][1]
        for tutor in list_all_tutors:
            subjects_tutor = list_all_tutors[tutor][0]
            grades_tutor = list_all_tutors[tutor][1]
            if subject_student in subjects_tutor and grade_student <= grades_tutor:
                name_tutor = list_all_tutors[tutor][2]
                name_student = student

                day = list_all_tutors[tutor][3][0]
                list_all_tutors[tutor][3].remove(day)
                hour = list_all_tutors[tutor][4][0]
                list_all_tutors[tutor][4].remove(hour)
                if len(list_all_tutors[tutor][3]) == 0 :
                    list_all_tutors.pop(tutor)
                list_outputs.append(f'Student {name_student}: you have {subject_student} lesson with {name_tutor} on {day} at {hour}:00.')
                found_matching_tutor = True
        if not found_matching_tutor:
            list_outputs.append(
                f'Student {name_student}: we could not find a matching tutor for {subject_student}.')











dict = {'yael':['math',3]}
matching_student_to_tutor(dict)
