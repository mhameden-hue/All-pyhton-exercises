km_o_urban=int(input('x:\n'))
km_w_urban=int(input('y:\n'))
fuel_consumption_o=(km_o_urban*5.1)/100
fuel_consumption_w=(km_w_urban*7.5)/100
total_consumption=round(fuel_consumption_o+fuel_consumption_w,2)
print('o=',fuel_consumption_w,'l')
print('w=',fuel_consumption_o,'l')
print('total_consumption=',total_consumption,'l')