import datetime
value = datetime.datetime.now()
print(value.strftime('%Y年%m月%d日'))
print(value.strftime('%H:%M:%S'))

print("[上下の血圧を入力してください]")
print("※家庭血圧を基にしています")

value1 = input("上の数値：")
value2 = input("下の数値：")

value1 = float(value1)
value2 = float(value2)

if 135 <= value1:
  print("あなたは高血圧です")
  print("×")
elif 85 <= value2:
  print("あなたは高血圧です")

elif 134 >= value1 > 101:
  print("正常値〇")
elif 84 >= value2 > 61:
  print("正常値〇")

else:
  print("あなたは低血圧です")

% matplotlib inline
import matplotlib.pyplot as plt

x = [100, 200, 300, 400, 500, 600]
y1 = [10, 20, 30, 50, 80, 130]
y2 = [10, 15, 30, 45, 60, 75]

fig = plt.figure()

# 1行2列に分割した中の1(左側)
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(x, y1, marker="o", color = "red", linestyle = "--")

# 1行2列に分割した中の2(右側)
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(x, y2, marker="v", color = "blue", linestyle = ":");