class Car:
  def __init__(self, make, model, year):
      self.make = make  
      self.model = model 
      self.year = year  

  def display_info(self):
      return f"{self.year} {self.make} {self.model}"

my_car = Car("Mercedes-Benz", "G63", 2018) 

print(my_car.display_info()) 
