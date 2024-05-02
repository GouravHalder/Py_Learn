from collections import deque

"""It is also possible to use a list as a queue, 
where the first element added is the first element retrieved (“first-in, first-out”); 
however, lists are not efficient for this purpose. """
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)
queue.popleft()  
queue.pop()
print(queue)