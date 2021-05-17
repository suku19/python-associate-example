from collections import deque

queue = deque(["Eric", "Jhon", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
queue.popleft()
print(queue)

