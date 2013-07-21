'''
Created on 2013-3-27

@author: luyang
'''

class Dough:
  '''
    Interface: Dough
  '''
  def __str__(self):
    pass
  
class Sauce:
  '''
    Interface: Sauce
  '''
  def __str__(self):
    pass
  
class Veggies:
  '''
    Interface: Veggies
  '''
  def __str__(self):
    pass
  
class Cheese:
  '''
    Interface: Cheese
  '''
  def __str__(self):
    pass

class Pepperoni:
  '''
    Interface: Pepperoni
  '''
  def __str__(self):
    pass

class Clam:
  '''
    Interface: Clam
  '''
  def __str__(self):
    pass

class Pizza:
  '''
    Abstract Class: Pizza
  '''
  def __init__(self):
    if self.__class__ == Pizza:
      raise NotImplementedError, \
          'Cannot create object of class Pizza'
    self._name = ''
    self._dough = None
    self._sauce = None
    self._veggies = []
    self._cheese = None
    self._pepperoni = None
    self._clam = None
    
  def __str__(self):
    result = '---- %s ----\n' % (self._name)
    if self._dough is not None:
      result += str(self._dough)
    if self._sauce is not None:
      result += str(self._sauce)
    if self._cheese is not None:
      result += str(self._cheese)
    if self._veggies:
      for i in self._veggies[:-1]:
        result += str(i)
        result += ', '
      result += self._veggies[-1]
    if self._clam is not None:
      result += str(self._clam)
    if self._pepperoni is not None:
      result += str(self._pepperoni)
    return result
  def getName(self):
    return self._name
  
  def setName(self, name):
    self._name = name
    
  def prepare(self):
    '''
      abstract interface
    '''
    if self.__class__ == Pizza:
      raise NotImplementedError, \
          'Cannot call prepare() of class Pizza'
    
  def bake(self):
    print 'Bake for 25 minutes at 350'
    
  def cut(self):
    print 'Cutting the pizza into diagonal slices'
    
  def box(self):
    print 'Place pizza in official PizzaStore box'

class PizzaStore:
  '''
    Abstract Class: PizzaStore
  '''
  def __init__(self):
    if self.__class__ == PizzaStore:
      raise NotImplementedError, \
          'Cannot create object of class PizzaStore'
    
  def _createPizza(self, item):
    '''
      abstract interface
    '''
    if self.__class__ == Pizza:
      raise NotImplementedError, \
          'Cannot call _createPizza() of class PizzaStore'
    
  def orderPizza(self, pizzaType):
    pizza = self._createPizza(pizzaType)
    print '--- Making a %s ---' % pizza.getName()
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    return pizza 

if __name__ == '__main__':
  pass