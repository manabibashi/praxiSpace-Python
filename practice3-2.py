"""
練習問題3. ガチャのプログラムを作る②（別の答えの例）
"""

import random

# あたった数を数える変数を作ります。
win_count = 0

# 0か1をランダムに作り、結果を足します。
win_count += random.randint(0, 1)
win_count += random.randint(0, 1)
win_count += random.randint(0, 1)

# 結果（あたった数）を出力します。
print(f"{win_count}回あたり")
