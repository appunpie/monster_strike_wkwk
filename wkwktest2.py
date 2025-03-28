#わくわくの実を厳選するシチュエーションを再現
#周回数の目安とどの方法が最適か調べる

#特級以上の実は96種類、そのうち特Lは32種類
#特級＞特級Ｍ＞特級Ｌの順に排出確率が大きくなるため、扱う乱数を９６種類から１９２種類に変更
#1~32：特級L
#33~96：特級M
#97~192：特級（無印）
random_wkwk = []
for i in range(1, 97):
    random_wkwk.append(i)
for i in range(33, 97):
    random_wkwk.append(i)
for i in range(65, 97):
    random_wkwk.append(i)
random_wkwk = sorted(random_wkwk)  #上のわくわくの特級の出現確率を再現した
#print(random_wkwk)

#一度の周回で獲得できるわくわくの実は12個
#注意※ アイテム宝箱は使用しないものとする、運極のハコ数は2個、チャンスバトルの出現は考えないものとする


#➁厳選したいをわくわくの実をリストアップし、その獲得してはステッキで付け替える方法

import random

test2 = [1, 2, 3, 4, 5, 5, 6, 6, 6, 8, 9, 10, 11, 11, 12, 13, 22, 23, 24, 24, 25, 26, 28, 28, 29, 29, 30, 30, 31, 32]

def wkwktest2(data):
    loop_num = 0  #周回回数を記録する変数
    known_num_list = []  #既出のわくわくの実を収容するリスト
    complete_num = []  #厳選キャラの取得済みのわくわくの実を収容するリスト
    while len(complete_num) < len(data):  #リストアップしたわくわくの実を厳選するまで、探索を続ける
        check_flag = False
        for j in range(12):  #一回の周回で12個獲得することを再現
            num = random.randint(0, 191)
            num1 = random_wkwk[num]  #上の方で作った確率再現リスト内の要素を乱数で抽出する
            if num1 in data and num1 not in known_num_list:  #該当する実であり、かつまだ獲得していない実であること
                complete_num.append(num1)
                check_flag = True
            
        if check_flag:
            known_num_list = []  #該当する実を獲得すると記憶をリセット
            loop_num += 1  #周回回数を+1
        else:
            loop_num += 1  #周回回数を+1
    return loop_num  #周回回数を表示

print(wkwktest2(test2))
                
                

            
                
        
        






