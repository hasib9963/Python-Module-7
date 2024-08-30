# function is a first class object
def double_decker():
    print('Starting the double decker')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun

# print(double_decker())
# print(double_decker()())

def do_something(work):
    print('work started') 
    # print(work) 
    work()
    print('work ended') 

# do_something(2)
# do_something('Ami onek busy')
def coding():
    print('Coding in Python')

# do_something(coding)
def sleeping():
    print('i am sleeping now.')

do_something(sleeping)