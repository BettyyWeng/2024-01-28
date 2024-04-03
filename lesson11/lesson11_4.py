import csv

students = [{'國文': 52, '數學': 53, '英文': 79},
            {'國文': 100, '數學': 57, '英文': 56},
            {'國文': 69, '數學': 96, '英文': 95},
            {'國文': 54, '數學': 87, '英文': 94},
            {'國文': 93, '數學': 64, '英文': 94},
            {'國文': 100, '數學': 91, '英文': 60},
            {'國文': 60, '數學': 94, '英文': 69},
            {'國文': 55, '數學': 65, '英文': 52},
            {'國文': 68, '數學': 51, '英文': 81},
            {'國文': 100, '數學': 100, '英文': 100}]

fileName = input('請輸入檔案名稱:') 
csvName = f'{fileName}.csv'

with open(csvName, mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['國文','數學','英文'])
    writer.writeheader()
    writer.writerows(students)

print(f'{csvName}存檔完成')
