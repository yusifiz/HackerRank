def staircase(n):
    for stairs in range(1, n + 1):
        print(' ' * (n - stairs) + '#' * stairs)
    
staircase(6)