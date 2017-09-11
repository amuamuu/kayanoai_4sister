import random

# おねえちゃん
sister = ['遠山りん', '佐倉慈', '棗ニナ', '保登モカ', 'ライネ']


# レアリティ
rare = ['[N]', '[R]', '[SSR]', '[UR]']

# n連ガチャ
n = input('何回引く？:')
for i in range(int(n)):
    print(random.choice(rare) + random.choice(sister))
