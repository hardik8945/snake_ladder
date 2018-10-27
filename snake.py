
#snake and ladder


from PIL import Image 
from random import randint

end=99

def show_board():
    img=Image.open('snake.jpg')
    img.show()
    
def check_ladder(points):
    if points==60:
        print("ladder")
        return 27
    elif points==9:
        print("ladder")
        return 58
    elif points==20:
        print("ladder")
        return 30
    elif points==25:
        print("ladder")
        return 57
    elif points==53:
        print("ladder")
        return 72
    elif points==54:
        print("ladder")
        return 85
    elif points==1:
        print("ladder")
        return 82
    else:
        return points
    

def check_snake(points):
    if points==43:
        print("snake")
        return 16
    elif points==5:
        print("snake")
        return 34
    elif points==70:
        print("snake")
        return 48
    elif points==78:
        print("snake")
        return 42
    elif points==95:
        print("snake")
        return 73
    elif points==96:
        print("snake")
        return 8812
    else:
        return points
    

def reached_end(points):
    if points==100:
        return True
    else:
        return True
    
def play():
    show_board()
    p1_name=input("Enter Player 1 Name: ")
    p2_name=input("Enter Player 2 Name: ")
    pp1=0 #initial points of players -  0
    pp2=0
    turn=0
    while(1):
        if turn%2==0:
            print(p1_name,"your turn: ")
            c=int(input("Press 1 for Continue, else 0: "))
            if c==0:
                print(p1_name,":",pp1)
                print(p2_name,":",pp2)
                print("Quitting the game!!!")
                break
            dice =randint(1,6)
            print("Dice showed: ",dice)
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if pp1>=end:
                pp1=end
            print(p1_name, ":" ,pp1)
            turn+=1
            if reached_end(pp1):
                print(p1_name, "won")
                break
        else:
            print(p2_name,"your turn: ")
            c=int(input("Press 1 for Continue, else 0: "))
            if c==0:
                print(p1_name,":",pp1)
                print(p2_name,":",pp2)
                print("Quitting the game!!!")
                break
            dice = randint(1,6)
            print("Dice showed: ",dice)
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if pp2>=end:
                pp2=start
            turn+=1
            print(p2_name, ":" ,pp2)
            if reached_end(pp2):
                print(p2_name, "won")
                break
