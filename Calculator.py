print("**CALCULATOR**")
choice=int(input("Enter your choice:n")) 
#User's choice [1,2,3,4]if choice is not in range of 1 to 4 print error message
print("Enter two numbers: ")
num1=int(input())
num2=int(input())
if choice == 1:#To add two numbers
  res=num1+num2
  print("Result=",res)
elif choice==2:#To substract two numbers
  res=num1-num2
  print("Result=",res)
elif choice==3:#To multiply two numbers
  res=num1*num2
  print("Result=",res)
elif choice==4:#To divide two numbers
  res=num1/num2
  print("Result=",res)
elif choice==5:
    exit()
        
