def find_max(scores):
    biggest = scores[0]
    for i in range(1, len(scores) - 1):    # 마지막을 안 봅니다
        if scores[i] > biggest:
            biggest = scores[i]
    return biggest

