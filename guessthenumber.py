i=0
n=9
num=20
while(True):
    userinput = input("please enter the number:")
    if(i<=9):
         if int(userinput)>num:
           print("user input is greater then correct number")
         elif int(userinput)< num:
           print("user input is less then correct number")
         else:
           print("Congratulations you have won")
           break
         i=i+1
         print("you have attempt left",n-i)
         continue
    else:
        print("Try again you have reached the limit")
        break


