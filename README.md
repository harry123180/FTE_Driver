# FTE_Driver
FTE控制器、架構、通訊、接線、範例程式、操作說明
首先介紹主控制器，它經由USB轉RS232的線，
將電腦的串列資料(Serail data)傳入主控器。

主控器在將傳入的資料轉成CANBus格式，發送給驅動器運動指令。
主控器實際樣子 

![image](https://github.com/harry123180/FTE_Driver/blob/main/%E4%B8%BB%E6%8E%A7%E6%8E%A5%E7%B7%9A%E5%9C%96Main%20controller%20Wiring%20Diagram.jpg)

主控器圖示 Main Controller Pin
如下圖


![image](https://github.com/harry123180/FTE_Driver/blob/main/%E4%B8%BB%E6%8E%A7%E5%99%A8%E5%9C%96%E7%A4%BAMain%20controller%20Diagram.png)

接下來介紹驅動器，驅動器的功用是連接馬達，控制馬達的轉角、或轉速，以下圖是驅動器。
驅動器實際圖示

![image](https://github.com/harry123180/FTE_Driver/blob/main/%E9%A9%85%E5%8B%95%E5%99%A8%E8%85%B3%E4%BD%8D%E5%9C%96Driver%20Pin%20Diagram.jpg)

驅動器腳位示意圖

![image](https://github.com/harry123180/FTE_Driver/blob/main/%E9%A9%85%E5%8B%95%E5%99%A8%E5%9C%96%E7%A4%BADriver%20Diagram.png)

