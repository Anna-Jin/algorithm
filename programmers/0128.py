# 완주하지 못한 선수
def solution4(participant, completion):
    for x in completion:
        if x in participant:
            participant.remove(x)

    answer = participant[0]
    return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution4(participant, completion))