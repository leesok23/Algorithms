# Version 1
def solution(seoul):
    return '김서방은 {}에 있다'.format(seoul.index('Kim'))


# Version 2
def solution(seoul):
    for i, name in enumerate(seoul):
        if name == 'Kim':
            return '김서방은 ' + str(i) + '에 있다'
