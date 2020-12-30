import serial #導入serial 串列模塊

COM_PORT = '/dev/ttyUSB1'  # 請自行修改序列埠名稱 依使用電腦去做區別
BAUD_RATES = 115200 #鮑率設定 廠商的設計，規定要115200

ser = serial.Serial(COM_PORT, BAUD_RATES) #設定串列傳輸物件 名稱就叫ser
########################################以下程式區塊是換算 把10進制轉16進制
def ItoHex(d):
    m4 = d // 16777216  # 取商數
    r1 = d % 16777216  # 取餘數
    m3 = r1 // 65536  # 取商數
    r2 = r1 % 65536  # 取餘數
    m2 = r2 // 256  # 取商數
    m1 = r2 % 256  # 取餘數
    return m4, m3, m2, m1
#########################################
def motor_move(N, pls, spd, packet):
    spd2 = spd // 256
    spd1 = spd % 256
    mot4, mot3, mot2, mot1 = ItoHex(int(pls))
    if (mot4 < 0): mot4 = mot4 + 256
    packet.append(0xaa)  ##開始
    packet.append(0x02)  ##模式 0x02為位置控制模式
    packet.append(N)  ##幾號機
    packet.append(spd2)  # RPM上限定義
    packet.append(spd1)  # RPM上限定義
    packet.append(mot4)  # 脈衝數定義
    packet.append(mot3)
    packet.append(mot2)
    packet.append(mot1)  # 脈衝數定義
    packet.append(0xee)  ##END
    # compute negative value
    ser.write(packet) #將指令寫入到主控器上
packet = bytearray() #創一個空的陣列 類型是bytearray
motor_move(1,1000,200,packet) #(N號馬達，脈衝位置(Plus)，轉速(RPM)，空的陣列(用於儲存指令碼))