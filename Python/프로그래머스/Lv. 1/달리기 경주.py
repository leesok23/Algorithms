def solution(players, callings):
    player_dict = {key: value for value, key in enumerate(players)}
    for calling in callings:
        curr = player_dict[calling]
        prior = curr - 1
        player_dict[players[curr]] -= 1
        player_dict[players[prior]] += 1
        players[curr], players[prior] = players[prior], players[curr]
    return players
