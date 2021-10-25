class Customer: 

    def __init__(self, n, a, p):
        self.__name = n
        self.__address = a
        self.__phone = p

    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_phone(self, phone):
        self.__phone = phone 

    
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_phone(self):
        return self.__phone

class Car:

    def __init__(self, ma, mo, y):
        self.__make = ma
        self.__model = mo
        self.__year = y

    def set_make(self, make):
        self.__make = make
    def set_model(self,model):
        self.__model = model
    def set_year(self, year):
        self.__year = year

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_year(self):
        return self.__year

class ServiceQuote:

    def __init__(self, pc, lc):
        self.__parts_charges = pc
        self.__labor_charges = lc
        self.__sales_tax = 0
        #self.__total_charges = 0

    def set_parts_charges(self, parts_charges):
        self.__parts_charges = parts_charges
    def set_labor_charges(self, labor_charges):
        self.__labor_charges = labor_charges
    
    def get_parts_charges(self):
        return self.__parts_charges
    def get_labor_charges(self):
        return self.__labor_charges
    def get_sales_tax(self):
        self.__sales_tax = float(self.__parts_charges + self.__labor_charges)*.12
        return self.__sales_tax
    def get_total_charges(self):
        total = self.__parts_charges + self.__labor_charges + str(self.__sales_tax)
        return total


