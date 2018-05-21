# 2.模拟斗地主发牌，扑克牌共54张：
#     花色：
#         黑桃('\u2660')
#         梅花('\u2663')
#         方块('\u2665')
#         红桃('\u2666')
#     数值：
#         A2-10JQK
#     大小王
#     三个人，每人发17张牌，底牌留三张：
#         输入回车，打印第一个人的17张牌
#         输入回车，打印第二个人的17张牌
#         输入回车，打印第三个人的17张牌
#         再输入回车，打印出三张底牌
import random


def show_cards(cards):
    order_dict = {'C':1,
                  'c':2,
                  '2':3,
                  'A':4,
                  'K':5,
                  'Q':6,
                  'J':7,          
                  '1':8,
                  '9':9,
                  '8':10,
                  '7':11,
                  '6':12,
                  '5':13,
                  '4':14,
                  '3':15}
    return sorted(cards,key = lambda x:(order_dict[x[2]],x[0]),reverse = True)

decks = [(y+' '+ x) for x in (list('A23456789JQK')+['10']) for y in ["\u2660","\u2663","\u2665","\u2666"]]
# print (decks)
decks += ['jocker','JOCKER']
random.shuffle(decks)
first_deck = show_cards(decks[0:17])
second_deck = show_cards(decks[17:34])
third_deck = show_cards(decks[34:51])

print('第一个人',' '.join(first_deck))
print('第二个人',' '.join(second_deck))
print('第三个人',' '.join(third_deck))
print('三张底牌',' '.join(decks[51:54]))