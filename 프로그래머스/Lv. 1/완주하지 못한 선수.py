# Version 1
def solution(participant, completion):
    participant.sort()
    completion.sort()
    i = 0
    while i < len(completion):
        if participant[i] != completion[i]:
            return participant[i]
        i += 1
    return participant[-1]


# Version 2
import collections

def solution(participant, completion):
    answer = collections.Counter(participant)-collections.Counter(completion)
    return list(answer)[0]
