"""
練習問題4. ガチャのプログラムを作る③（別の答えの例）
"""

import random

# あたった数を数える変数を作ります。
win_count = 0

# ガチャを引く回数を指定します。
n = 10

# 指定した回数ガチャを引き、結果を足します。
for _ in range(n):
    win_count += random.randint(0, 1)

# 結果（あたった数）を出力します。
print(f"{win_count}回あたり")
