"""
くり返す
"""

# リストを作ります。
animals = ["ネコ", "イヌ", "ネコ"]

# リスト内のデータを先頭から順に取り出します。
for animal in animals:
    # 実行する中身は半角4文字分字下げします。
    print(animal)
    # 結果は ネコ イヌ ネコ

# 4回くり返します。
for i in range(4):
    print(i)  # 結果は 0 1 2 3

# range()で作った数字は使わなくてもよいです。
for _ in range(4):
    print("?")  # 結果は ? ? ? ?
