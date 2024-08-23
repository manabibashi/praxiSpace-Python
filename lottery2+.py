"""
w2. くじ引きのプログラムを作る。

3回くじを引き、結果を画面に出します。
くじは、0がはずれ、1があたりです。
"""

import random

# あたった数を数えます。
win_count = 0

# 3回くじを引きます。この場合、毎回の結果は残りません。
win_count += random.randint(0, 1)
win_count += random.randint(0, 1)
win_count += random.randint(0, 1)

# あたった数を画面に出します。
print(f"{win_count}回あたりました。")
