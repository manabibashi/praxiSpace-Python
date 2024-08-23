"""
5. if文を使う。

場面ごとに処理を切り替えることができます。
"""

# 0以上5未満のランダムな整数を作ります。
import random

x = random.randint(0, 5)
print(f"x: {x}")

# xが1の場合は処理します。
if x == 1:
    print("1です。")

# xが2未満かによって処理を切り替えます。
if x < 2:
    print("2未満です。")
else:
    print("2以上です。")

# xが2未満か4未満かによって処理を切り替えます。
if x < 2:
    print("2未満です。")
elif x < 4:
    print("4未満です。")
else:
    print("4以上です。")
