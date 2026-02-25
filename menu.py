while True:
  print("---Menu---")
  print("1. cm to ft")
  print("2.km to miles")
  print("3.USD to INR")
  print("4.exit")
  choice=int(input("enter your choice (1,4)"))
  if choice==1:
    cm=float(input("enter value in cm"))
    ft=cm/30.48
    print(cm,"cm=",ft,"ft")
  elif choice==2:
    km=float(input ("enter value in km "))
    miles=km*0.621371
    print(km,"km=",miles,"miles")
  elif choice==3:
    USD=float(input("enter value in USD"))
    INR=USD*83
    print(USD, "USD=",INR,"INR")
  elif choice==4:
      print("program exited")
      break
  else:
      print("invalid choice! please try again .")