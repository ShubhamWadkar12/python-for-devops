"""name = input("Enter your name : ")
person = f"Hello World, My name is {name} and i will be king of the pirates"
other_name = ("Globe")
print(person.replace("World",other_name))"""


def check_os(opsystem):
    if opsystem == "Windows":
        print("Switch to linux")
    elif opsystem == "Linux" or opsystem == "Mac":
        print("you are good to go")
    
for i in range(1,10):
    check_os("Windows")