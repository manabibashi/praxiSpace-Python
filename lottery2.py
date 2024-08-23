"""
w2. くじ引きのプログラムを作る。

3回くじを引き、結果を画面に出します。
くじは、0がはずれ、1があたりです。
"""

import random

# くじを引いた結果を入れるリストを作ります。
results = []

# 3回くじを引きます。
results.append(random.randint(0, 1))
results.append(random.randint(0, 1))
results.append(random.randint(0, 1))

# 結果を画面に出します。
print(results)

# あたった数を数えます。
win_count = results.count(1)

# あたった数を画面に出します。
print(f"{win_count}回あたりました。")
