from random import randint

name = input('please input ur name:')
f = open('game.txt', encoding='gbk')
lines = f.readlines()
f.close()
scores = {}
for i in lines:
    s = i.split()
    scores[s[0]] = s[1:]
score = scores.get(name)
if score is None:
    score = [0,0,0]

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = total_times / game_times

else:
    avg_times = 0

print(f'{name}, 你已经进行{game_times}次 ，最少{min_times}次， 平均{avg_times}次')

num = randint(1, 100)
times = 0
print('Guess it')
bingo = False
while bingo == False:
    times += 1
    answer = int(input())
    if answer > num:
        print('Too Big')
    elif answer < num :
        print('Too Small')
    else:
        print('Bingo')
        bingo = True
if game_times == 0 or times < min_times:
    min_times = times
total_times += times
game_times += 1

scores[name] = [str(game_times), str(min_times), str(total_times)]
print(f'{name}, 你已经进行{game_times}次 ，最少{min_times}次， 平均{avg_times}次')
result = ''
for i in scores:
    line = i + ' ' + ' '.join(scores[i]) + '\n'
    result += line

f = open('game.txt', 'w', encoding='gbk')
f.write(result)
f.close()
