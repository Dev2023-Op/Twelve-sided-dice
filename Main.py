from random import randint
results = []
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
twelve = 0

for j in range(1001):
  a = randint(1, 6)
  b = randint(1, 6)
  c = a + b
  print(str(a) + " + " + str(b) + " = " + str(c))
  results.append(c)
  if c == 1:
    one += 1
  elif c == 2:
    two += 1
  elif c == 3:
    three += 1
  elif c == 4:
    four += 1
  elif c == 5:
    five += 1
  elif c == 6:
    six += 1
  elif c == 7:
    seven += 1
  elif c == 8:
    eight += 1
  elif c == 9:
    nine += 1
  elif c == 10:
    ten += 1
  elif c == 11:
    eleven += 1
  elif c == 12:
    twelve += 1

print("one: " + str(one))
print("two: " + str(two))
print("three: " + str(three))
print("four: " + str(four))
print("five: " + str(five))
print("six: " + str(six))
print("seven: " + str(seven))
print("eight: " + str(eight))
print("nine: " + str(nine))
print("ten: " + str(ten))
print("eleven: " + str(eleven))
print("twelve: " + str(twelve))
