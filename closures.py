def power(exponent):
    
    def inner(base):
        return base ** exponent
    
    return inner

power_of_two = power(2)
power_of_three = power(3)

print(power_of_two(5))
print(power_of_three(5))

decorators
