import random

def generate_code(n=8):
    number='0123456789'
    code= ''.join(random.choice(number) for x in range(n))
    return code