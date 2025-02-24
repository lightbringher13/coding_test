def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    intersection = lost_set & reserve_set
    lost_set = lost_set - intersection
    reserve_set = reserve_set - intersection
    for student in sorted(lost_set):
        if student - 1 in reserve_set:
            reserve_set.remove(student - 1)
            lost_set.remove(student)
        elif student + 1 in reserve_set:
            reserve_set.remove(student + 1)
            lost_set.remove(student)
    return n - len(lost_set)
