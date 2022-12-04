import random

random_number = random.randint(1,100)
# print(random_number)

game_count = 1

while True: 
    try:
        my_number = int(input("1~100 choose number:"))
    
        if my_number > random_number:
            print("down") 
        elif my_number < random_number:
            print("up")
        elif my_number == random_number:
            print(f"congratuation. {game_count}회 만에 맞췄습니다.")
            break
            
        game_count = game_count+1
    
    except:
        print("error, put only number")
        
        
        