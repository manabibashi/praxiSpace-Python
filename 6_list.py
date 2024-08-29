"""
データをまとめる
"""

# データを指定してリストを作ります。
animals = ["ネコ", "イヌ", "ネコ"]

# リストの中身をすべて出力します。
print(animals)

# 空のリストを作ります。
fruits = []

# リストにデータを追加します。
fruits.append("リンゴ")
fruits.append("バナナ")

# リスト内の1つ目のデータを出力します。
print(animals[0])

# リスト内の2つ目のデータを出力します。
print(animals[1])

# リスト内の最後のデータを出力します。
print(animals[-1])

# リスト内の長さ（データの数）を数えます。
print(len(animals))

# リスト内の特定のデータの数を数えます。
print(animals.count("ネコ"))

# リストから特定のデータを消します。
# （いくつかある場合は1つ目を消します）
animals.remove("ネコ")

print(animals)
