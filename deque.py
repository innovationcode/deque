class Deque(object):
  def __init__(self):
    self.items = []
    self.count = 0
  # Front
  def add_to_front(self, item):
    self.items.insert(0, item)
    self.count += 1
  def remove_from_front(self):
    self.count -= 1
    return self.items.pop(0)
  # Rear 
  def add_to_rear(self, item):
    self.items.append(item)
    self.count += 1
  def remove_from_rear(self):
    self.count -= 1
    return self.items.pop()

  def size(self):
    return self.count

  def isEmpty(self):
    return self.size == 0

  def printDeque(self):
    for item in self.items:
      print(item , end = " -> ")

dq = Deque()
dq.add_to_front(10)
dq.add_to_front(20)
dq.add_to_front(30)
print("Size = ", dq.size())
dq.add_to_rear(100)
dq.add_to_rear(200)
dq.add_to_rear(300)
print("Size = ", dq.size())
dq.printDeque()

print("\nDq front   :  ", dq.remove_from_front())
print("\nDq front   :  ", dq.remove_from_rear())

print("Size = ", dq.size())


