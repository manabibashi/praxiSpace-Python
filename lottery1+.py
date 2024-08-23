"""
w1. くじ引きのプログラムを作る。

1回くじを引き、結果を画面に出します。
くじは、0がはずれ、1があたりです。
"""

import random

# 0が"はずれ"、1が"あたり"です。
outcomes = ["はずれ", "あたり"]

# 1回くじを引きます。
result = random.randint(0, 1)

# 結果を画面に出します。
print(outcomes[result])
