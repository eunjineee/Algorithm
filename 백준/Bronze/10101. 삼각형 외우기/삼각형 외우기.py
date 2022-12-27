a3 = 0
ans = 0
li = []
for i in range(3):
  a = int(input())
  if a == 60:
    a3 += 1
  li.append(a)
  ans += a
if a3 == 3:
  print('Equilateral')
else:
  if ans != 180:
    print('Error')
  else:
    if len(set(li)) ==3:
      print('Scalene')
    else:
      print('Isosceles')