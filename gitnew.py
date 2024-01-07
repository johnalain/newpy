#https://youtu.be/smKHKgedkP4 time: 2:03:00
# class Human:
#     name = input('enter ur name: ')
#     if name == 'michel':
#         print('welcome')
        
#     else:
#         print('error')
    
# if u enter michel print welcome ir u print another name output error

# x = 3
# y = 7
# res = x+y
# print (res)

# class Home:
#     #inside class functions must have self
#     def kitch(self):
#         print('for cooking and eating')
    
#     def bedroom(self):
#         print('for sleeping and relaxing')
        
# x = Home()
# x.kitch()
# x.bedroom()

# for cooking and eating
# for sleeping and relaxing

class Home:
    #create function to let execution automatic
    def __init__(self):
        self.kitch()
        self.bedroom()
    def kitch(self):
        print('for cooking and eating')
    
    def bedroom(self):
        print('for sleeping and relaxing')
x = Home()
    

        

 

