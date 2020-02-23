# 20-02-19
# EX 30.7

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*args):
    scores = sorted(list(args))
    return scores[0], scores[-1]

def get_average(korean, english, mathematics, science):
    scores = (korean, english, mathematics, science)
    return sum(scores) / len(scores)

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.f}'.format(min_score, max_score, average_score))
