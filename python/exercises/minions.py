# from collections import Counter

# def minion_game(string):
'''Run Time error on some '''
#     # your code goes here
#     player1 = 'Stuart'
#     player2 = 'Kevin'
#     score1, score2 = 0, 0
    
#     #for i, s in enumerate(string):
#     ss = [string[i:j + 1] for i in range(len(string))\
#             for j in range(i,len(string))]
#     ss_count = Counter(ss)
#     vowels = 'aeiou'
#     for s in ss_count.keys():
#         if s[0] in vowels:
#             score2 += ss_count[s]
#         else:
#             score1 += ss_count[s]
    
#     if score1 > score2:
#         print(player1 + ' ' + str(score1))
#     elif score1 < score2:
#         print(player2 + ' ' + str(score2))
#     else:
#         print('Draw')
    
    
VOWELS = 'AEIOU'

def minion_game(string):
    stew_score = 0
    kev_score = 0
    for i in range(0, len(string)):
        points = len(string) - i
        if string[i] in VOWELS:
            kev_score += points
        else:
            stew_score += points

    if stew_score > kev_score:
        print(f"Stuart {stew_score}")
    elif kev_score > stew_score:
        print(f"Kevin {kev_score}")
    else:
        print("Draw")     

if __name__ == '__main__':
    s = input('enter the string:')
    minion_game(s)