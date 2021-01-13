import serial #導入serial 串列模塊
COM_PORT = 'COM5'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES) #設定串列傳輸物件 名稱就叫ser
spd = [0,0,0,0] # spd的數量代表你有幾顆馬達要讀 像這邊定義了四個 代表你有四個馬達要讀


def hextodex(alist):
    a2 = alist[0]
    a1 = alist[1]
    # print(alist)
    dd = 256 * a2 + a1
    if (dd > 32767):
        dd = dd - pow(2, 16)
    return dd
while True:
    if (ser.readline(1) == b'\xee'):
        msg = []

        for j in range(9):
            msg.append(ser.readline(1))
        new = [int.from_bytes(msg[3], byteorder='big', signed=False),
               int.from_bytes(msg[4], byteorder='big', signed=False)]
        # print(msg)
        # t_pos = hextodex(new)
        if (msg[2] == b'\x01'): #msg[2]這一位代表回授回來的訊息是第幾號馬達的
            spd[0] = hextodex(new) #各自放入屬於它們陣列位置上
        elif (msg[2] == b'\x02'):
            spd[1] = hextodex(new)
        elif (msg[3] == b'\x03'):
            spd[2] = hextodex(new)
        elif (msg[4] == b'\x04'):
            spd[3] = hextodex(new)
            # print(msg)
        print(spd)