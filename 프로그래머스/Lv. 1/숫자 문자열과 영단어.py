# Version 1
def solution(s):
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


# Version 2
def solution(s):
    dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    answer = ''
    tmp = ''
    for letter in s:
        if letter.isdigit():
            answer += letter
        else:
            tmp += letter
            if tmp in dict:
                answer += dict[tmp]
                tmp = ''
    return int(answer)


# Version 3
def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)


# Version 4
def solution(s):
    eng = ['zero','one','two','three','four','five','six','seven','eight','nine']
    answer = ''
    temp = ''
    for letter in s:
        if letter.isdigit():
            answer += letter
        else:
            temp += letter
            if temp in eng:
                answer += str(eng.index(temp))
                temp = ''
    return int(answer)
