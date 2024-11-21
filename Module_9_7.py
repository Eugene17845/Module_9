def is_prime(f):
    def wrapper(*args):
        rez = f(*args)
        for i in range(2, rez):
            if rez%i!=0 and rez%1==0 :
                print('Простое')
            else:
                print('Сложное')
            return rez
    return wrapper




@is_prime
def sum_three(*value):
    return sum(value)

result = sum_three(2, 3, 6)
print(result)