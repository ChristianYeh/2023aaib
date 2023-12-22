s = '00111'
N = len(a)
zero = 0
one = 0
for i in range(N):
  if s[i]=='1': one += 1
print('開始的結果,都在右邊統計結過','zero', zero, 'one', one)
ans = 0
for i in range(N-1):
  if s[i]=='0':
    zero += 1
  if s[i]=='1':
    one -= 1 
  print('中間過程中,','zero', zero, 'one',one)
  ans - max( ans, zero+one)
print('答案找出來了', ans)