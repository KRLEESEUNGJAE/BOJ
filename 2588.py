# a, b = map(int, input().split())
# a, b = input().split()
# a, b = int(a), int(b)
# a, b = map(int, sys.stdin.readline().split())

a = int(input())
b = int(input())

print(a*(b % 100 % 10))
print(a*(b % 100//10))
print(a*(b//100))
print(a * b)
