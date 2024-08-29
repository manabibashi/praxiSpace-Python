"""
練習問題3. ガチャのプログラムを作る②（答えの例）
"""

import random

# ガチャの結果を入れるリストを作ります。
results = []

# 0か1をランダムに作り、結果をリストに加えます。
results.append(random.randint(0, 1))
results.append(random.randint(0, 1))
results.append(random.randint(0, 1))

# あたった数（1の数）を数え、結果を出力します。
win_count = results.count(1)
print(f"{win_count}回あたり")
