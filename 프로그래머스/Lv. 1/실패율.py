# Version 1
def solution(N, stages):
    result = {}
    players = len(stages)
    for stage in range(1,N+1):
        if players > 0:
            count = stages.count(stage)
            result[stage] = count / players
            players -= count
        else:
            result[stage] = 0
    
    return sorted(result, key=lambda x: result[x], reverse=True)


# Version 2 (works but runs time error)
def solution(N, stages):
    failure = []
    players = len(stages)
    for i in range(1,N+1):
        failed_players = stages.count(i)
        failure.append(failed_players / players)
        players -= failed_players

    return sorted(range(1,len(failure)+1), key=lambda x: failure[x-1], reverse=True)


# Version 3 (works but runs time error)
def solution(N, stages):
    n_failure = [0] * N
    for stage in stages:
        if stage <= N:
            n_failure[stage-1] += 1
    
    rate_failure = []
    players = len(stages)
    for i in range(len(n_failure)):
        rate_failure.append(n_failure[i]/(players-sum(n_failure[:i])))
    
    return sorted(range(1,len(rate_failure)+1), key=lambda x: rate_failure[x-1], reverse=True)
