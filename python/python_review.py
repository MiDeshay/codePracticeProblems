from collections import deque

d = deque([4,5,6,7,8])

my_list = [1,2,3,4,5]

my_dict = {
    1: "a",
    2: "b",
    3: "c", 
    4: "d"
    }

# del my_dict[1]

# my_dict[1] = "A"

# print(my_dict.keys())


my_list.append(6)

my_list.insert(0, 1)

my_list.insert(0, 0)

my_list.pop()

my_list.pop(0)


d.appendleft(3)

d.append(9)

d.pop()

d.popleft()

print(my_list)
