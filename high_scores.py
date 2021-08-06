def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    a = sorted(scores)
    a.reverse()
    le = len(scores)
    if le == 1 or le == 2:
        return a
    else :
        return a[0:3]
