class car:
    def _init_(self,model,make,year):
        self.model = model
        self.make = make
        self.year = year

#getters
         
    def get_model(self):
        return self.model
    
    def get_make(self):
        return self.make
    
    def get_year(self):
        return self.year
    
#objects
car_1 = car ("demio","nissan","2018")
car_2 = car ("hilux","toyota","2020")
car_3 = car ("premio","range","2022")

print(car_1.get_model())
print(car_1.get_make())
print(car_1.get_year())



  
print(car_2.get_model())
print(car_2.get_make())
print(car_2.get_year())

  
print(car_3.get_model())
print(car_3.get_make())
print(car_3.get_year())

  