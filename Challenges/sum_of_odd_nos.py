def sumofoddnumbers(a, b):
    j = 0
    for i in range(a,b)[1:]:
      if i%2 == 0:
        continue
      else:
        j += i
    return j

#tests
x = sumofoddnumbers(30,4090)
print(x)
