def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp1 = ''
        while arr1[i] > 0:
            tmp1 += str(arr1[i] % 2)
            arr1[i] //= 2
        tmp2 = ''
        while arr2[i] > 0:
            tmp2 += str(arr2[i] % 2)
            arr2[i] //= 2
            
        if len(tmp1) < n:
            tmp1 += (n-len(tmp1))*'0'
        if len(tmp2) < n:
            tmp2 += (n-len(tmp2))*'0'
            
        tmp1 = tmp1[::-1]
        tmp2 = tmp2[::-1]
        tmp = ''
        for j in range(n):
            if tmp1[j]=='1' or tmp2[j]=='1':
                tmp += '#'
            else:
                tmp += ' '

        answer.append(tmp)
        
    return answer
