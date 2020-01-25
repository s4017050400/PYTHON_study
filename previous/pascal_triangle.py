#巴斯卡三角形
#Pascal's triangle


#　　　　　　　　１
#　　　　　　　１　１
#　　　　　　１　２　１
#　　　　　１　３　３　１
#　　　　１　４　６　４　１
#　　　１　５　10　10　５　１
#　　１　６　15　20　15　６　１
#　１　７　21　35　35　21　７　１
#１　８　28　56　70　56　28　８　１



def tangle(n):
    L=[1]
    x=0
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L,L+[0])]
        x += 1
        if x==n:
            break
            
            
#result

for i in tangle(10):
    print(i)

[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

#----------------------------------------------------------

#yield
  #https://openhome.cc/Gossip/Python/YieldGenerator.html
#zip
  #https://www.runoob.com/python3/python3-func-zip.html
