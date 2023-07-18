# Version 1
def solution(s):
    words = s.split(' ')
    answer = []
    for word in words:
        temp = ''
        for i,letter in enumerate(word):
            if i%2==0:
                temp += letter.upper()
            else:
                temp += letter.lower()
        answer.append(temp)
    return ' '.join(answer)


# Version 2
def solution(s):
    return ' '.join(map(lambda x: ''.join([a.upper() if i%2==0 else a.lower() for i,a in enumerate(x)]), s.split(' ')))


# Version 3
def solution(s):
    return ' '.join(''.join([x.upper() if i%2==0 else x.lower() for i,x in enumerate(word)]) for word in s.split(' '))
