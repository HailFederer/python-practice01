# 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'
print('\''+'\', \''.join(s[1:].split('/'))+'\'')
# s = s[1:]
# s = s.split('/')
# for index, path in enumerate(s):
#     if index != len(s)-1:
#         print('\''+path+'\'', end=', ')
#     else:
#         print('\'' + path + '\'')
# for index, path in enumerate(s):
#     if index != 0:
#         print('\''+path+'\'', sep=', ', end='')
print()

# 디렉토리 경로명과 파일명을 분리하여 출력하세요.

s = '/usr/local/bin/python'
print('\''+'\', \''.join(s.rsplit('/', 1))+'\'')
# s = s.rsplit('/',1)
# for index, path in enumerate(s):
#     if index != len(s)-1:
#         print('\'' + path + '\', ', end='')
#     else:
#         print('\'' + path + '\'')