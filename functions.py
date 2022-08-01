'''Functions'''
'''Function itself calling is called Recursion'''
'''In function - we need to call the functions'''


# def a():      # Function declaration
#     print('niharika')
# a()  # Function calling

# def b(n):
#     print('hello '+n)
# b('hii') # hello hii

'''we can add multiple times'''
# def b(n):
#     print('hello '+n)
# b('how r u')    #  hello how r u
# b('what r u doing')  # hello what r u doing


'''we can add many arguments using * to list & tuples'''
# def c(*v):
#     print('my favourite colors',v)
# c('black','green','merron')  #  my favourite colors ('black', 'green', 'merron')
# c(['pink','purple'])  # my favourite colors (['pink', 'purple'],)

'''Also we can add many list arguments using slicing method'''
# def d(v):
#     print('my favourite colors '+str(v[:]))
# d(['black','green','merron'])    #  my favourite colors ['black', 'green', 'merron']
# d('black','green','merron') # we can't add tuples to string using slicing

# def m(r,p):
#     print('my name is',r,'and i am practicing',p)
# m('niharika','functions')   #  my name is niharika and i am practicing functions

# def m(r,p):
#     print('my name is',r,'and i am practicing',p)
# m('niharika','functions')      #  my name is niharika and i am practicing functions
# m(r='niharika',p='functions')  #  my name is niharika and i am practicing functions
# m(p='functions',r='niharika')  #  my name is niharika and i am practicing functions

# def m(r,p):
#     print('my name is',r,'and i am practicing',p)
# r=input()
# p=input()
# m(r,p)              # my name is niharika and i am practicing functions

# def hi(a,b):
#     return(a,b)
# print(hi(4,5))         # (4, 5)

# def c(a,b):
#     return(a+b,a*b)
# a=int(input())
# b=int(input())
# print(c(a,b))          #  (6, 8)

# def c(a,b):
#     return(a+b,a*b,b-a)
# a=int(input())
# b=float(input())
# print(c(a,b))       #   (9.0, 20.0, 1.0)

# def c(a,b):
#     return(a+b,a*b,b-a)
# a=float(input())
# b=float(input())
# print(c(a,b))       #  (7.0, 12.0, 1.0)
