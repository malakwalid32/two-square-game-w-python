from dataclasses import replace
board=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"] 
num=0
def displayboard():
    print(board[1]+"  | ",board[2]+"  | ",board[3]+"  | ",board[4]+"  | ")
    print("----------------------")
    print(board[5]+"  | ",board[6]+"  | ",board[7]+"  | ",board[8]+"  | ")
    print("----------------------")
    print(board[9]+"  | ",board[10]+" | ",board[11]+" | ",board[12]+" | ")
    print("----------------------")
    print(board[13]+" | ",board[14]+" | ",board[15]+" | ",board[16]+" | ")


def player1():
       num1= int(input("player one please enter your first number: "))
       num2= int(input("player one please enter your second number: "))
       if num1==num2 :
              print("please enter two different numbers")
              player1()
              
       elif  board[num1 ]==board[num2 - 1 ] or board[num1 ] ==board[num2 - 4 ] or board[num2  ]==board[num1 - 1 ] or board[num2  ]==board[num1 - 4 ] and num>0 and num<16 and board[num1]!="x" or board[num2]!="x":
              board[num1]="x"
              board[num2]="x"
       else:
              print("please enter two valid numbers" )
              player1()
       displayboard()
       check_1()
       
              
def player2 ():

       num3= int(input("player two please enter your first number: "))
       num4= int(input("player two please enter your second number: "))
       
       if num3==num4:
              print("please enter two different numbers")
              player2()

       elif  board[num3 ]==board[num4 - 1 ] or board[num3 ] ==board[num4 - 4 ] or board[num4  ]==board[num3 - 1 ] or board[num4  ]==board[num3 - 4 ] and num>0 and num<16 and board[num3]!="x" or board[num4]!="x":
              board[num3]="x"
              board[num4]="x"
       else: 
              print("please enter two valid numbers")
              player2 ()
       displayboard()
       check_2()
def check_1():
       if  (board[1]=="1"and board[2]=="2") or (board[1]=="1" and board[5]=="5") or (board[2]=="2" and board[3]=="3") or (board[2]=="2" and board[6]=="6") or (board[3]=="3" and board[4]=="4") or (board[4]=="4" and board[8]=="8") or (board[5]=="5" and board[6]=="6") or (board[6]=="6" and board[10]=="10") or (board[6]=="6" and board[7]=="7") or (board[5]=="5" and board[9]=="9") or (board[7]=="7" and board[8]=="8") or (board[3]=="3" and board[7]=="7") or (board[7]=="7" and board[8]=="11") or (board[8]=="8" and board[12]=="12") or (board[9]=="9" and board[10]=="10") or (board[9]=="9" and board[13]=="13") or (board[10]=="10" and board[11]=="11") or (board[10]=="10" and board[14]=="14") or (board[11]=="11" and board[12]=="12") or (board[11]=="11" and board[15]=="15") or (board[12]=="12" and board[16]=="16") or (board[13]=="13" and board[14]=="14") or (board[14]=="14" and board[15]=="15") or (board[15]=="15" and board[16]=="16"):
              player2()
       elif board[1]=="x"   and board[2]=="x"   and board[3]=="x"   and board[4]=="x"   and board[5]=="x"   and board[6]=="x"   and board[7]=="x"   and board[8]=="x"   and board[9]=="x"   and board[10]=="x"   and board[11]=="x"   and board[12]=="x"   and board[13]=="x"   and board[14]=="x"   and board[15]=="x"   and board[16]=="x":   
              print("Draw")
              exit()
       else:
              print("player1 wins")
              exit()      
       return
def check_2():
       if  (board[1]=="1"and board[2]=="2") or (board[1]=="1" and board[5]=="5") or (board[2]=="2" and board[3]=="3") or (board[2]=="2" and board[6]=="6") or (board[3]=="3" and board[4]=="4") or (board[4]=="4" and board[8]=="8") or (board[5]=="5" and board[6]=="6") or (board[6]=="6" and board[10]=="10") or (board[6]=="6" and board[7]=="7") or (board[5]=="5" and board[9]=="9") or (board[7]=="7" and board[8]=="8") or (board[3]=="3" and board[7]=="7") or (board[7]=="7" and board[8]=="11") or (board[8]=="8" and board[12]=="12") or (board[9]=="9" and board[10]=="10") or (board[9]=="9" and board[13]=="13") or (board[10]=="10" and board[11]=="11") or (board[10]=="10" and board[14]=="14") or (board[11]=="11" and board[12]=="12") or (board[11]=="11" and board[15]=="15") or (board[12]=="12" and board[16]=="16") or (board[13]=="13" and board[14]=="14") or (board[14]=="14" and board[15]=="15") or (board[15]=="15" and board[16]=="16"):
              player1()
       elif board[1]=="x"   and board[2]=="x"   and board[3]=="x"   and board[4]=="x"   and board[5]=="x"   and board[6]=="x"   and board[7]=="x"   and board[8]=="x"   and board[9]=="x"   and board[10]=="x"   and board[11]=="x"   and board[12]=="x"   and board[13]=="x"   and board[14]=="x"   and board[15]=="x"   and board[16]=="x":   
              print("Draw")
              exit()
       else:
              print("player2 wins")
              exit()       
       return
def playgame():
       displayboard()
       n_actions=0
       while n_actions <=8 :
              player1()
              displayboard()
              check_1()
playgame()              