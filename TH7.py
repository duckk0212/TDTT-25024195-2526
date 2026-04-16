"""
counter = 1
def show_counter():
    print("Current counter:", counter)  
def bad_increment():
    counter = counter + 1  
    print("Bad_increment:", counter)
def good_increment():
    global counter         
    counter = counter + 1
    print("Good_increment:", counter)
    
show_counter()
bad_increment()
good_increment()
"""



"""
import name_student
if __name__ == "__main__":
    print(name_student.name)
    print(name_student.get_address())
"""


"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b
    """

