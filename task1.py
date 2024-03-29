def a_plus_b(a, b, max_X):
    result = a * a * max_X + b
    return result
#2190003_강민아
x = 2
y = 1
h = 10
print(f'Y = a^2X + b')
print(f'a: {x}')
print(f'b: {y}')
print(f'MAx: {h}')
for max_X in range(11):  # max_X를 0부터 10까지 반복
    z = a_plus_b(x, y, max_X)
    print(f'{x}*{x}*{max_X} + {y} = {z}')
