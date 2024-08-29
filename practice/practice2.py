"""
練習問題2. ガチャのプログラムを作る①（答えの例）
"""

# 0 か 1 をランダムに作ります。
import random

result = random.randint(0, 1)

# 1 の場合は「あたり」、
# 0 の場合は「はずれ」と出力します。
if result == 1:
    print("あたり")
else:
    print("はずれ")
