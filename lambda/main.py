def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(4)
mytripler = myfunc(5)

print(mydoubler(12)) 
print(mytripler(12))