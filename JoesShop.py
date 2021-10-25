import JoesClass as jc

customer = jc.Customer('Annabelle Herschend', '1492 Columbus Ave', '404-405-4067')
car = jc.Car('Porsche', 'Cayenne', '2024')
sq = jc.ServiceQuote('395','129')
print()
print('Customer Information:')
print('Customer Name:',customer.get_name())
print('Address:', customer.get_address())
print('Phone Number:',customer.get_phone())
print()
print('Car Information:')
print('Make:',car.get_make())
print('Model:', car.get_model())
print('Year:', car.get_year())
print()
print('Pricing:')
print('Parts Charges:',sq.get_parts_charges())
print('Labor Charges:', sq.get_labor_charges())
print('Sales Tax (12%):', sq.get_sales_tax())
print('Total Charges:', sq.get_total_charges())
print()


