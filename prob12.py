# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보세요. 1부터 99까지만 실행하세요.


# def game(string):
#     for i in range(len(string)):
#         x = string[i:i + 1]
#         if x == '3' or x == '6' or x == '9':
#             return True
#     return False
#
# evens = [i for i in range(1, 101) if game(str(i)) == True]
# print(evens)


# for num in range(1, 1000):
#     flag = False
#     clap = ''
#     strNum = str(num)
#     for index in range(len(strNum)):
#         digit = strNum[index : index+1]
#         if digit == '3' or digit == '6' or digit == '9':
#             flag = True
#             clap += '짝'
#     if flag == True:
#         print(strNum +' '+ clap)


# def game(num):
#     clap = ''
#     for index in range(len(num)):
#         digit = num[index : index+1]
#         if digit == '3' or digit == '6' or digit == '9':
#             clap += '짝'
#     return clap
#
#
# for num in range(1, 1000):
#     strNum = str(num)
#     clap = game(strNum)
#     if clap != '':
#         print('{0:3} {1}'.format(int(strNum), clap))

for n in range(1, 1000):
    s = str(n)
    c = s.count('3') + s.count('6') + s.count('9')
    if c < 1:
        continue

    print("{0} {1}".format(s, '짝'*c))







