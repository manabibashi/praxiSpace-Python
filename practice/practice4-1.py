"""
練習問題4. ガチャのプログラムを作る③（答えの例）
"""

import random

# ガチャの結果を入れるリストを作ります。
results = []

# ガチャを引く回数を指定します。
n = 10

# 指定した回数ガチャを引き、結果をリストに加えます。
for _ in range(n):
    results.append(random.randint(0, 1))

# あたった数（1の数）を数え、結果を出力します。
win_count = results.count(1)
print(f"{win_count}回あたり")
