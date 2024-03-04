import random

min = 1
max = 100
guess = random.randint(min,max)
count = 0

print("=====猜數字遊戲======\n\n")
#print(f'要猜的數字是{guess}')

while(True):
    try:
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count +=1
        if(keyin<=max and keyin >=min):
            if (keyin == guess):
                print(f"Bingo!你猜對了，答案是:{guess}")
                print(f"您猜了{count}次了")
                break
            elif keyin > guess:
                print("再小一點")
                max = keyin - 1
            elif keyin < guess:
                print("再大一點")
                min = keyin +1
        else:
            print("超出範圍")
    except:
        print("輸入格式錯誤")
        count +=1
    print(f"您已經猜了{count}次")
print("遊戲結束")