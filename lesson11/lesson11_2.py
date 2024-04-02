import pyinputplus as pyip
from random import randint
from pprint import pprint

nums = pyip.inputInt("請輸入學生數量:")

students:list[dict] = []
for _ in range(nums):
    student:dict[str,int] = {}
    for subject in ['國文','英文','數學']:
        student[subject] = randint(50,100)
    students.append(student)
pprint(students)