import random
def game():
 num=random.randint(1, 3)
 return (num)
def check(v):
 if v==1:
  print(f1)
 elif v==2:
  print(f2)
 else:
  print(f3)
file0=open("Jackpot.txt","r")
jack=file0.read()
file0.close()
file1=open("chk1.txt","r")
check1=file1.read()
file1.close()
file2=open("chk2.txt","r")
check2=file2.read()
file2.close()
file5=open("fig1.txt","r")
f1=file5.read()
file5.close()
file6=open("fig2.txt","r")
f2=file6.read()
file6.close()
file7=open("fig3.txt","r")
f3=file7.read()
file7.close()
if check1==check2:
  print ("......Hello User.......")
  file3=open("banner.txt","r")
  ban=file3.read()
  print(ban)
  file3.close()
  print("This Script is written by {} ".format(check1))
  print("Follow me on Instagam: user_unknown_005")
  file4=open("wallet.txt","r")
  money=file4.read()
  file4.close()
  money=int(money)
  print("Your present sum is $:{}".format(money))
  print("You need to pay $5 for each game")
  print("Enter 1 to continue and 0 to exit")
  void=int(input())
  while void == 1:
   if money<=5:
    print("You are given a loser's allowance of $100")
    money=money+100
   money=money-5
   num1=game()
   num2=game()
   num3=game()
   check(num1)
   check(num2)
   check(num3)
   if num1==num2:
    if num1==num3:
     print(jack)
     print("CONGRATULATIONS")
     print("YOU WON $115 for winning")
     money=money+115
   void=int(input("Enter 1 to play again and 0 to quit"))
  print("remaining money in wallet {}".format(money))
  print("Saving Your Progress")
  file8=open("wallet.txt","w")
  money=str(money)
  file8.write(money)
  file8.close()
  print("Done")
