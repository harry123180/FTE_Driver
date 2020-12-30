import serial #導入serial 串列模塊

COM_PORT = '/dev/ttyUSB1'  # 請自行修改序列埠名稱 依使用電腦去做區別
BAUD_RATES = 115200 #鮑率設定 廠商的設計，規定要115200

ser = serial.Serial(COM_PORT, BAUD_RATES) #設定串列傳輸物件 名稱就叫ser
#########################################
def motor_move_speed(N, spd, packet):
    spd2 = spd // 256
    spd1 = spd % 256

    if (spd2 < 0): spd2 = spd2 + 256
    packet.append(0xaa)  ##開始
    packet.append(0x01)  ##模式 0x01為位速度控制模式
    packet.append(N)  ##幾號機
    packet.append(spd2)  # RPM上限定義
    packet.append(spd1)  # RPM上限定義
    packet.append(0x00)  # 脈衝數定義
    packet.append(0x00)
    packet.append(0x00)
    packet.append(0x00)  # 脈衝數定義
    packet.append(0xee)  ##END
    # compute negative value
    ser.write(packet) #將指令寫入到主控器上
packet = bytearray()#創一個空的陣列 類型是bytearray
#spd的參數值在-32,768 to 32,767 在輸入的時候麻煩考慮到物理極限 不要把馬達炸了
motor_move_speed(1,200,packet) #(N號馬達,轉速(RPM)，空的陣列(用於儲存指令碼)) 如要反轉 就把轉速參數 加上一個-號