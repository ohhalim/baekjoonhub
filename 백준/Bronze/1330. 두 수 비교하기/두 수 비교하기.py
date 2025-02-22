A, B = map(int, input().split())

if A > B:
    print(f'>')
elif A < B:
    print(f'<')
elif A == B:
    print(f"==")