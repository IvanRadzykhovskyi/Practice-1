card_number_str = input('Enter your credit card\'s number: ')
last_digits_str = card_number_str[-4:]
print(last_digits_str)
last_digits_str = last_digits_str[:-1]
sum_ = 0
for i in last_digits_str:
    sum_ += int(i)

print(sum_)