#!/usr/bin/python3
def multiple_returns(sentence):
    tupp = (0, '')
    if sentence == '':
        return 0, None
    else:
        lis = list(tupp)
        lis[0] = len(sentence)
        lis[1] = sentence[0]
        tupp = tuple(lis)
        return tupp[0], tupp[1]
