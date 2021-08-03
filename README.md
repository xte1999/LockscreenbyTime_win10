# LockscreenbyTime_win10
A python program in win10.  
1. You can set the time to lock the computer(by setting  year, month, day), 
2. Fullscreen pictures will show when you lock screen.

## Code Usage :
1. Opening Lock_screen_data.json and writing the date to set deadline. For example, rectify the json to [2021, 8, 2, 9, 20, 35] 
which means the unlock time is 2021/8/2/9:20
2. Adding pictures to directory ./pictures, added pictures will show per 12 seconds.
3. run lock_screen_simple.py
4. Keyboard and screen will be locked, when you click the set time is reached, the program will close.

## 界面效果
![view1](https://user-images.githubusercontent.com/50430387/127969048-99a11408-e3ce-4ce6-a167-756e8e2bc2f3.jpg)

## 打包程序+开机启动
1. 使用pyinsatller打包程序为exe格式
2. 在注册表“计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon”的Userinit项中添加打包程序位置 这样开机就会运行程序 **要注意小心操作**
3. 重新启动电脑，点击屏幕后开始判断，如未到解锁时间，则先显示结束时间后每12s换一次壁纸。
