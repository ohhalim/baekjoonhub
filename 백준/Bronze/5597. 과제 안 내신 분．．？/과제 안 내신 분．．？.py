def find_missing_students():
    all_students = set(range(1, 31))

    submitted = set()

    for _ in range(28):
        n = int(input())
        submitted.add(n)

    not_submitted = all_students - submitted

    not_submitted = sorted(not_submitted)

    for student in not_submitted:
        print(student)

find_missing_students()
