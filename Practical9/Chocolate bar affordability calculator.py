#define a function 
def calculator(total_money,price):
    number=total_money//price
    left=total_money%price
    return number, left

#example
total=1124
bar=26
numbers,change = calculator(total,bar)
 print(f'Bars:{numbers}, Change left over:{change}')
