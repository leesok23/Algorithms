def solution(keymap, targets):
    key_dict = {}
    for keymap_element in keymap:
        for i in range(len(keymap_element)):
            if keymap_element[i] not in key_dict or i+1 < key_dict[keymap_element[i]]:
                key_dict[keymap_element[i]] = i + 1
            
    answer = []
    for target in targets:
        count = 0
        for i in range(len(target)):
            if target[i] in key_dict.keys():
                count += key_dict[target[i]]
            else:
                answer.append(-1)
                break
            if i == len(target)-1:
                answer.append(count)
    return answer
