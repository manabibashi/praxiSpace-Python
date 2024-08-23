"""
w3. くじ引きのプログラムを作る。

指定した回数くじを引き、結果を画面に出します。
くじは、0がはずれ、1があたりです。
"""

import random

# くじを引く回数を指定します。
n = 10

# くじを引いた結果を入れるリストを作ります。
results = []

# n回くじを引きます。
for i in range(n):
    results.append(random.randint(0, 1))

# 結果を画面に出します。
print(results)

# あたった数を数えます。
win_count = results.count(1)

# あたった数を画面に出します。
print(f"{n}回のうち、{win_count}回あたりました。")
