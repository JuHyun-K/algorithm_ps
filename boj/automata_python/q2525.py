a, b = map(int, input().split())
c = int(input())

#hour
a += c//60
c %= 60

#min
b += c
a += b//60
b %= 60

#hour(24)
a %= 24
print(a, b)


#헐
t=h*60+m+int(input()) #시간도 분도, 다 분 취급
print(t//60%24,t%60) #나중에 다시 설정
