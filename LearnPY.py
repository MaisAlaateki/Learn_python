# for x in range(2,10):
#     for n in range(2,x):
#         if x%n == 0:
#             print(x,'equal',n,'*',x//n)
#             break
#     else:
#             #loop fell through without
#              print(x,'is a prime number')


################
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
# ask_ok('Do you really want to quit?')
###################
# n=2
# x=2
# if x%n == 0:
#     print(x,'equal',n,'*',x//n)
# else:
#     print('null')

def parrot(voltage, state='a stiff',action='voom'):
    print("__this is parot wouldn't ",action,end=' ')
    print("if you put",voltage,"volts through it." ,end=' ')
    print("E s",state,"!")
d = {"voltage": "four million","state":"bleedin' demised","action":"voom"}
parrot(**d)