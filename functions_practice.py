def hello():
    print("Hello User")

hello()
  
def pack ():
    print("swimsuit," "towel", "sunblock")

pack()

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")
        
eat_lunch([" a sandwich"])
eat_lunch(["an apple", "a cookie"])
eat_lunch([])
