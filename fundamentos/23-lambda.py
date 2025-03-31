# função de potencia de lambda
power = lambda num:num ** 2 

# verifica se o numero e par
is_even = lambda x: x % 2 == 0

# função que divide um numero por outro
div_num = lambda x, y: x / y

#função que inverte uma striung
reverse = lambda s: s [::-1]

print(power(8))
print(power(9))
print(is_even(23))
print(is_even(66))
print(div_num(10,2))
print(div_num(165,6))
print(reverse("Lucas"))