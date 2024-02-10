from random import *
class game:
    def __init__(self,name):
        self.player1=name
        self.player2='computer'
        self.about=['rock','paper','scissor']
    @staticmethod
    def check_validity(a):
        if(a>=0 and a<3):
            return True
        return False
    
    def display(self,a,b):
        print(f"{self.player1} ",a,"\n")
        print(f"{self.player2} ",b,"\n")
    def check_result(self,a,b):
        if(a==b):
            return 2
        elif((a==0 and b==2) or (a==1 and b==0)or(a==2 and b==1)):
            return 1
        else:
            return 0
    def play(self,point):
        point_player1=0
        point_player2=0
        while(point_player1!=point and point_player2!=point):
            print("\n----------------------------------------------\n")
            user_choice=int(input("enter\n0 for rock\n1 for paper\n2 for scissor : "))
            computer_choice=randint(0,2)
            c=self.check_validity(user_choice)
            if(c==False):
                print("wrong choice")
            else:
                s=self.check_result(user_choice,computer_choice)
                if(s==1):
                    print(f"computer choses {self.about[computer_choice]} , {self.player1} won!")
                    point_player1+=1
                elif(s==2):
                    print(f"computer choses {self.about[computer_choice]} , draw!")
                else:
                    print(f"computer choses {self.about[computer_choice]} , {self.player2} won!")
                    point_player2+=1
            self.display(point_player1,point_player2)
        if(point_player1==point):
            print(f"{self.player1} won the game ! ")
        else:
            print(f"{self.player2} won the game ! ")
            
name=str(input("enter your name : "))
point=int(input("enter the point you want to play : "))
a=game(name)
a.play(point)