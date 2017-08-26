score = 0

# 1問目
print('問題1　NEW GAME!に出てくるお姉ちゃんはだれ？ \n 1.保登モカ 2.佐倉慈 3.遠山りん 4.棗ニナ \n 数字で解答>>>')
sister_1 = input()
if sister_1 == '3':
    score += 100

# 2問目
print('問題2　がっこうぐらし！に出てくるお姉ちゃんはだれ？ \n 1.保登モカ 2.佐倉慈 3.遠山りん 4.棗ニナ \n 数字で解答>>>')
sister_2 = input()
if sister_2 == '2':
    score += 100

# 3問目
print('問題3　ご注文はうさぎですか？に出てくるお姉ちゃんはだれ？ \n 1.保登モカ 2.佐倉慈 3.遠山りん 4.棗ニナ \n 数字で解答>>>')
sister_3 = input()
if sister_3 == '1':
    score += 100

# 4問目
print('問題4　うらら迷路帖に出てくるお姉ちゃんはだれ？ \n 1.保登モカ 2.佐倉慈 3.遠山りん 4.棗ニナ \n 数字で解答>>>')
sister_4 = input()
if sister_4 == '4':
    score += 100

# 成績発表
if score == 400:
    print('全問正解！！')
elif score == 300:
    print('3問正解！')
elif score == 200:
    print('2問正解！')
elif score == 100:
    print('1問正解！')
else:
    print('不合格！')
