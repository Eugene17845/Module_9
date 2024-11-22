def is_prime(f):
    def wrapper(*args):
        list = ''
        rez = f(*args)
        for i in range(2, rez):
            g = rez % i == 0
            list += str(g)
        if 'True' not in list:
            print('Простое')
        else:
            print('Составное')

        return rez
    return wrapper




@is_prime
def sum_three(*value):
    return sum(value)

result = sum_three(1, 1, 8)
print(result)
