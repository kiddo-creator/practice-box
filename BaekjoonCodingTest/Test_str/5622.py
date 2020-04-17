​dial=input()
time=0
for c in dial:
    if c in ['A', 'B', 'C']:
        time += 3
    elif c in ['D', 'E', 'F']:
        time += 4
    elif c in ['G', 'H', 'I']:
        time += 5
    elif c in ['J', 'K', 'L']:
        time += 6
    elif c in ['M', 'N', 'O']:
        time += 7
    elif c in ['P', 'Q', 'R', 'S']:
        time += 8
    elif c in ['T', 'U', 'V']:
        time += 9
    elif c in ['W', 'X', 'Y', 'Z']:
        time += 10
print(time)
