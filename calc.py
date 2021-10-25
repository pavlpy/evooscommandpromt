while True:
  a = input().split()
  if(a[1] == "+"):
    print(int(a[0]) + int(a[2]))
  if(a[1] == "-"):
    print(int(a[0]) - int(a[2]))
  if(a[1] == "*"):
    print(int(a[0]) * int(a[2]))
  if(a[1] == "/"):
    print(int(a[0]) / int(a[2]))
  

