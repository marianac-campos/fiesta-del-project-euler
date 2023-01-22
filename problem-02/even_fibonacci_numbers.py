limit = 4000000
a = 2
b = 8
c = 34
sum = 10
while c < limit:
  sum += c
  a = b
  b = c
  c = 4 * b + a
  print(a,b,c)

print(sum)