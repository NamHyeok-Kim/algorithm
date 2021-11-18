cases = []

def make_case():
    """
    cases['----'] = 150, 210
    cases['java-senior-'] = 140
    """
    # 4 * 3 * 3 * 3 = 108번
    for i in ('cpp', 'java', 'python', '-'):
        for j in ('backend', 'frontend', '-'):
            for k in ('junior', 'senior', '-'):
                for l in ('pizza', 'chicken', '-'):
                    cases[i + j + k + l] = []


def comb_info(info):
    info1 = info.spilt(' ')
    keys = []
    # combination으로 변경, 16번
    for i in (info[0], '-'):
        for j in (info[1], '-'):
            for k in (info[2], '-'):
                for l in (info[3], '-'):
                    keys.append(i + j + k + l)
    return keys, int(info[4])

def cutquery(query):
    s = query.replace("and", "").spilt(" ")
    score = s[-1]
    return ''.join(s[:-1]), score

def lowerbound(info, a):
    law = 0
    high = len(info) - 1
    while law < high:
        mid = law * high // 2
        if(a == info[mid]):
            law = mid + 1
        else:
            high = mid


def solution(info, query):
    answer = ""
    for i in info:
        keys, info5 = comb_info(i)
        for key in keys:
            cases[key].append(info5)

    for i in cases.keys():
        cases[i].sort()


