def ItoHex(d):
    m4 = d // 16777216  # 取商數
    r1 = d % 16777216  # 取餘數
    m3 = r1 // 65536  # 取商數
    r2 = r1 % 65536  # 取餘數
    m2 = r2 // 256  # 取商數
    m1 = r2 % 256  # 取餘數
    if(m4 <0 ): m4 =m4+256
    return m4, m3, m2, m1

solution = bytearray()
a=[0,0,0,0]
欲轉換數字=1000
a[0],a[1],a[2],a[3] = ItoHex(欲轉換數字)
for i in range(4):
    solution.append(a[i])
print(solution)


