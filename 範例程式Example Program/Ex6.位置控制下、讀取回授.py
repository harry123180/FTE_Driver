import serial #導入serial 串列模塊
COM_PORT = '/dev/ttyUSB0'  # 請自行修改序列埠名稱
BAUD_RATES = 115200
ser = serial.Serial(COM_PORT, BAUD_RATES) #設定串列傳輸物件 名稱就叫ser
pos = [0,0,0,0] # Pos的數量代表你有幾顆馬達要讀 像這邊定義了四個 代表你有四個馬達要讀


def hextodex(alist):
    a4 = alist[0]
    a3 = alist[1]
    a2 = alist[2]
    a1 = alist[3]
    # print(alist)
    rr2 = 256 * a2 + a1
    rr1 = 65536 * a3 + rr2
    dd = 16777216 * a4 + rr1
    if (dd > 2147483647):
        dd = dd - pow(2, 32)
    return dd
while True:
    if (ser.readline(1) == b'\xee'):
        msg = []

        for j in range(9):
            msg.append(ser.readline(1))
        # new = [int(msg[3]),msg[4],msg[5],msg[6]]
        new2 = [msg[3], msg[4], msg[5], msg[6]]
        new = [int.from_bytes(msg[3], byteorder='big', signed=False),
               int.from_bytes(msg[4], byteorder='big', signed=False),
               int.from_bytes(msg[5], byteorder='big', signed=False),
               int.from_bytes(msg[6], byteorder='big', signed=False)]
        # print(msg)
        # t_pos = hextodex(new)
        if (msg[2] == b'\x01'): #msg[2]這一位代表回授回來的訊息是第幾號馬達的
            pos[0] = hextodex(new) #各自放入屬於它們陣列位置上
        elif (msg[2] == b'\x02'):
            pos[1] = hextodex(new)
        elif (msg[3] == b'\x03'):
            pos[2] = hextodex(new)
        elif (msg[4] == b'\x04'):
            pos[3] = hextodex(new)
            # print(msg)
        print(pos)