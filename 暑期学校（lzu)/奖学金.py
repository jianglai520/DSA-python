n = int(input())
student = []
sid = 0

for i in range(n):
    Chinese, Math, English = map(int, input().split())
    total = Chinese + Math + English
    sid += 1
    student.append((-total, -Chinese, sid, total))

sorted_student = sorted(student)

for i in range(5):
    item = sorted_student[i]
    print(item[2],item[3])
