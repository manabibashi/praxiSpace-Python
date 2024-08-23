"""
w1. くじ引きのプログラムを作る。

1回くじを引き、結果を画面に出します。
くじは、0がはずれ、1があたりです。
"""

import random

# 1回くじを引きます。
result = random.randint(0, 1)

# 1が出たらあたり、それ以外ははずれです。
if result == 1:
    print("あたり")
else:
    print("はずれ")
