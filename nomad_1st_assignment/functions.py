days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def is_on_list(a, b):
  return b in a

def get_x(a, b):
  return a[b]

def add_x(a, b):
  a.append(b)

def remove_x(a, b):
  a.remove(b)

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)