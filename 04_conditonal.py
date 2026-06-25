"""a = 90
b = 30
c = 50

if a > b and a > c :
    print("a is biggest")
else:
    print("b is bigger")
    
env = input("Enter the env : ")

if env == "dev":
    print("We are in dev")
elif env == "test":
    print("It is test env")
else:
    print("we are in prod")"""
    
    
    
#function
    
def check_biggest():
    env = input("Enter the env : ")
    if env == "dev":
         print("We are in dev")
    elif env == "test":
         print("It is test env")
    else:
         print("we are in prod")
check_biggest()


def add_num():
    a = int(input("Enter two numbers"))
    b = int(input("Enter two numbers"))
    print(a+b)
add_num()

def check_os(opsystem):
    if opsystem == "Windows":
        print("Switch to linux")
    elif opsystem == "Linux" or opsystem == "Mac":
        print("you are good to go")
    
for i in range(1,10):
    check_os("Windows")