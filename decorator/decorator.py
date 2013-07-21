'''
Created on 2013-3-12

@author: luyang
'''

class Beverage:
  '''
    Abstract Class: Beverage
  '''
  def __init__(self):
    if self.__class__ == Beverage:
      raise NotImplementedError, \
          'Cannot create object of class Beverage'
    self._description = 'Unknown Beverage'
  
  def getDescription(self):
    return self._description
  
  def cost(self):
    pass

class DarkRoast(Beverage):
  def __init__(self):
    Beverage.__init__(self)
    self._description = 'Dark Roast Coffee'
    
  def cost(self):
    return .99

class HouseBlend(Beverage):
  def __init__(self):
    Beverage.__init__(self)
    self._description = 'House Blend Coffee'
    
  def cost(self):
    return .89
  
class Espresso(Beverage):
  def __init__(self):
    Beverage.__init__(self)
    self._description = 'Espresso'
    
  def cost(self):
    return 1.99
  
class Decaf(Beverage):
  def __init__(self):
    Beverage.__init__(self)
    self._description = 'Decaf Coffee'
    
  def cost(self):
    return 1.05
  
class CondimentDecorator(Beverage):
  def __init__(self):
    if self.__class__ == CondimentDecorator:
      raise NotImplementedError, \
          'Cannot create object of class CondimentDecorator'
  
  def getDescription(self):
    pass
  
class Milk(CondimentDecorator):
  def __init__(self, beverage):
    CondimentDecorator.__init__(self)
    self.__beverage = beverage
    
  def getDescription(self):
    return self.__beverage.getDescription() + ', Milk'
  
  def cost(self):
    return .10 + self.__beverage.cost()
  
class Mocha(CondimentDecorator):
  def __init__(self, beverage):
    CondimentDecorator.__init__(self)
    self.__beverage = beverage
    
  def getDescription(self):
    return self.__beverage.getDescription() + ', Mocha'
  
  def cost(self):
    return .20 + self.__beverage.cost()  
  
class Soy(CondimentDecorator):
  def __init__(self, beverage):
    CondimentDecorator.__init__(self)
    self.__beverage = beverage
    
  def getDescription(self):
    return self.__beverage.getDescription() + ', Soy'
  
  def cost(self):
    return .15 + self.__beverage.cost()
  
class Whip(CondimentDecorator):
  def __init__(self, beverage):
    CondimentDecorator.__init__(self)
    self.__beverage = beverage
    
  def getDescription(self):
    return self.__beverage.getDescription() + ', Whip'
  
  def cost(self):
    return .10 + self.__beverage.cost()  
  
if __name__ == '__main__':
  beverage = Espresso()
  print beverage.getDescription() + ' $' + str(beverage.cost())
  
  beverage2 = DarkRoast()
  beverage2 = Mocha(beverage2)
  beverage2 = Mocha(beverage2)
  beverage2 = Whip(beverage2)
  print beverage2.getDescription() + ' $' + str(beverage2.cost())
  
  beverage3 = HouseBlend()
  beverage3 = Soy(beverage3)
  beverage3 = Mocha(beverage3)
  beverage3 = Whip(beverage3)
  print beverage3.getDescription() + ' $' + str(beverage3.cost())