def solution(progresses, speeds):
    days = []
    for progress, speed in zip(progresses, speeds):
        cnt = 0
        while progress < 100:
            progress = progress + speed
            cnt = cnt + 1
        days.append(cnt)
    print(days)

    start = days[0]
    release = []
    many = 1
    for i in range(1, len(days)):
        if days[i] <= start:
            many = many + 1
        else:
            release.append(many)
            start = days[i]
            many = 1
    release.append(many)
    return release
