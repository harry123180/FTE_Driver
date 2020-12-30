#麥輪控制模式一定要四顆馬達

import serial #導入serial 串列模塊

COM_PORT = '/dev/ttyUSB1'  # 請自行修改序列埠名稱 依使用電腦去做區別
BAUD_RATES = 115200 #鮑率設定 廠商的設計，規定要115200

ser = serial.Serial(COM_PORT, BAUD_RATES) #設定串列傳輸物件 名稱就叫ser
########################################以下程式區塊是換算 把10進制轉16進制
def ItoHex(d):
    m2 = d // 256  # 取商數
    m1 = d % 256  # 取餘數
    if(m2<0):m2 =m2+256
    return m2, m1
#########################################
def motor_move( FB, LR,R, packet):
    FB2,FB1 = ItoHex(FB)
    LR2,LR1 = ItoHex(LR)
    R2,R1 = ItoHex(R)
    packet.append(0xaa)  ##開始
    packet.append(0x03)  ##模式 0x03為麥輪控制模式
    packet.append(0x01)  ##幾號機在此模式下此位無意義
    packet.append(FB2)  # FB
    packet.append(FB1)  # FB
    packet.append(LR2)  # LR
    packet.append(LR1)  # LR
    packet.append(R2)  # R
    packet.append(R1)  # R
    packet.append(0xee)  ##END
    # compute negative value
    ser.write(packet) #將指令寫入到主控器上
packet = bytearray() #創一個空的陣列 類型是bytearray
motor_move(10,10,10,packet) #(Forward and Backward Speed ，Left and Right Speed , Rotate Speed ，空的陣列(用於儲存指令碼))