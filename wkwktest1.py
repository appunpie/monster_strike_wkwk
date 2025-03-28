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


#➀厳選したいキャラを一体ずつ確実に厳選していく方法

import random

test1 = [[1, 30, 22], [23, 31, 11], [2, 3, 6], [9, 8, 6], [25, 28, 30], [32, 13, 24], [12, 26, 29], [11, 10, 5], [4, 5, 6], [24, 28, 29]]  #データを乱数で適当に10体分作成できる



def wkwktest1(data):
    loop_num = 0  #周回回数を記録する変数
    for i in range(len(data)):  #厳選したキャラ分処理を行う

        complete_num = []  #厳選キャラの取得済みのわくわくの実を収容するリスト
        known_num_list = []  #既出の数字を保管して、その後に出た既出の数字を省く用
        while len(complete_num) < 3:  #3個のわくわくの実を厳選するまで、探索を続ける
            check_flag = False
            for j in range(12):  #一回の周回で12個獲得することを再現
                num = random.randint(0, 191)
                num1 = random_wkwk[num]  #上の方で作った確率再現リスト内の要素を乱数で抽出する
                if num1 not in known_num_list:  #既出のわくわくの実ではないか判定
                    known_num_list.append(num1)
                    if num1 in data[i] and num1 not in complete_num:  #該当する実であり、かつまだ獲得していない実であること
                        complete_num.append(num1)
                        check_flag = True
            
            if check_flag:
                known_num_list = []  #該当する実を獲得すると記憶をリセット
                loop_num += 1  #周回回数を+1
            else:
                loop_num += 1  #周回回数を+1
    return loop_num  #周回回数を表示

print(wkwktest1(test1))
                
                

            
                
        
        






