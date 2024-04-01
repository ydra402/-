def input_scores():
    student_scores = []
    for i in range(5):
        student = {}
        student['학번'] = input('학번: ')
        student['이름'] = input('이름: ')
        student['영어'] = int(input('영어: '))
        student['C-언어'] = int(input('C-언어: '))
        student['파이썬'] = int(input('파이썬: '))
        student_scores.append(student)
    return student_scores

def calculate_total_average(student_scores):
    for student in student_scores:
        student['총점'] = student['영어'] + student['C-언어'] + student['파이썬']
        student['평균'] = student['총점'] / 3

def calculate_grade(student_scores):
    for student in student_scores:
        if student['평균'] >= 90:
            student['학점'] = 'A+'
        elif student['평균'] >= 80:
            student['학점'] = 'A'
        elif student['평균'] >= 70:
            student['학점'] = 'B+'
        elif student['평균'] >= 60:
            student['학점'] = 'B'
        else:
            student['학점'] = 'F'

def calculate_rank(student_scores):
    sorted_scores = sorted(student_scores, key=lambda x: x['총점'], reverse=True)
    for i, student in enumerate(sorted_scores):
        student['등수'] = i + 1

def print_scores(student_scores):
    print('성적관리 프로그램')
    print('=' * 80)
    print('학번\t\t이름\t\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수')
    print('=' * 80)
    for student in student_scores:
        print(f"{student['학번']}\t{student['이름']}\t\t{student['영어']}\t{student['C-언어']}\t{student['파이썬']}\t{student['총점']}\t{student['평균']:.2f}\t{student['학점']}\t{student['등수']}")

student_scores = input_scores()
calculate_total_average(student_scores)
calculate_grade(student_scores)
calculate_rank(student_scores)
print_scores(student_scores)

# 50 55 80
# 80 70 60
# 50 90 75
# 60 80 65
# 100 90 80
# 1234567890 김철수
# 1234567891 이영희
# 1234567892 박지성
# 1234567893 오현수
# 1234567894 권영민