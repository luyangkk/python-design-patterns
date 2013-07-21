'''
Created on 2013-3-12

@author: luyang
'''

class Pizza:
  '''
    Abstract Class: Pizza
  '''
  def __init__(self):
    if self.__class__ == Pizza:
      raise NotImplementedError, \
          'Cannot create object of class Pizza'
    self._name = ''
    self._dough = ''
    self._sauce = ''
    self._toppings = []
    
  def getName(self):
    return self._name
  
  def prepare(self):
    print 'Preparing %s' % self._name
    
  def bake(self):
    print 'Baking %s' % self._name
    
  def cut(self):
    print 'Cutting %s' % self._name
    
  def box(self):
    print 'Boxing %s' % self._name
      
class CheesePizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'Cheese Pizza'
    self._dough = 'Regular Crust'
    self._sauce = 'Marinara Pizza Sauce'
    self._toppings.append('Fresh Mozzarella')
    self._toppings.append('Parmesan')  
    
class PepperoniPizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'Pepperoni Pizza'
    self._dough = 'Crust'
    self._sauce = 'Marinara Sauce'
    self._toppings.append('Sliced Pepperoni')
    self._toppings.append('Sliced Onion')
    self._toppings.append('Grated Parmesan Cheese')  
      
class ClamPizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'Clam Pizza'
    self._dough = 'Thin Crust'
    self._sauce = 'White Garlic Sauce'
    self._toppings.append('Clams')
    self._toppings.append('Grated Parmesan Cheese')
    
class VeggiePizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'Veggie Pizza'
    self._dough = 'Crust'
    self._sauce = 'Marinara Sauce'
    self._toppings.append('Shredded Mozzarella')
    self._toppings.append('Grated Parmesan')
    self._toppings.append('Diced Onion')
    self._toppings.append('Sliced Mushrooms')
    self._toppings.append('Sliced Red Pepper')
    self._toppings.append('Sliced Black Olives')
      
class SimplePizzaFactory:
  def createPizza(self, pizzaType):
    pizza = None   
    if pizzaType == 'cheese':
      pizza = CheesePizza()
    elif pizzaType == 'pepperoni':
      pizza = PepperoniPizza()          
    elif pizzaType == 'clam':
      pizza = ClamPizza()
    elif pizzaType == 'veggie':
      pizza = VeggiePizza()
    return pizza  
      
class PizzaStore:
  def __init__(self, factory):
      self.__factory = factory
      
  def orderPizza(self, pizzaType):
    pizza = self.__factory.createPizza(pizzaType)
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    return pizza

if __name__ == '__main__':
  factory = SimplePizzaFactory()
  store = PizzaStore(factory)
  
  pizza = store.orderPizza("cheese")
  print 'We ordered a %s' % pizza.getName()
  
  pizza = store.orderPizza("veggie")
  print 'We ordered a %s' % pizza.getName()