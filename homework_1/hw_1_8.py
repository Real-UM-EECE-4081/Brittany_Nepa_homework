#Solve the Tower of Hanoi problem

def TowerOfHanoi(n, start, end, placeholder):
    if n == 1:
        print("Move first disc from start", start, "to end position", end)
        return
    TowerOfHanoi(n-1, start, placeholder, end)
    print("Move disk", n, "from start", start, "to ending position", end)
    TowerOfHanoi(n-1, placeholder, end, start)

n = 3
TowerOfHanoi(n, 'A', 'B', 'C')

