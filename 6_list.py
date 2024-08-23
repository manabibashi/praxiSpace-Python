"""
6. リストを使う。

リストは数値や文字の集まりです。
"""

# リストを作ります。
animals = ["ネコ", "イヌ", "ネコ"]

# リストの中身を画面に出します。リストの番号は0から始まります。
print(animals[0])
print(animals[1])
print(animals[2])

# リストの長さを画面に出します。
print(len(animals))

# リストの中にある値の個数を数えます。
print(animals.count("ネコ"))

# リストに値を追加します。
animals.append("ウマ")

# リストの最後を画面に出します。
print(animals[3])
print(animals[-1])  # 後ろから数えた場合は-1です。

# リストから値を取り除きます。
animals.remove("ウマ")
