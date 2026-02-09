class Queue:

    def __init__(self):
        
        self.__queue=[]

    def add(self,item):
        self.__queue.append(item)
    
    def next(self):
       print(self.__queue.pop(0)) 

    def is_empty(self):
       True if self.__queue.len==0 else False


queue=Queue()

queue.add('Alice')
queue.add('Bob')
queue.add('Louise')

queue.next()