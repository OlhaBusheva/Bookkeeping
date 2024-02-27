eq = input('Please enter your equation: ')

eq_replaced = (
    eq.replace('(', '')
    .replace(')', '')
    .replace('x^2', '')
    .replace('x', '')
    .replace('=', '+')
    .split('+')
)

a = int(eq_replaced[0].strip())
b = int(eq_replaced[1].strip())
c = int(eq_replaced[2].strip())

print(a, b, c)

x_1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x_2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print(x_1, x_2)
