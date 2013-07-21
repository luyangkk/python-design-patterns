'''
Created on 2013-3-19

@author: luyangkk
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
    print 'Tossing dough...'
    print 'Adding sauce...'
    print 'Adding toppings: '
    for t in self._toppings:
      print '   %s' % t
    
  def bake(self):
    print 'Bake for 25 minutes at 350'
    
  def cut(self):
    print 'Cutting the pizza into diagonal slices'
    
  def box(self):
    print 'Place pizza in official PizzaStore box'
  
class NYStyleCheesePizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'NY Style Sauce and Cheese Pizza'
    self._dough = 'Thin Crust Dough'
    self._sauce = 'Marinara Sauce'
    self._toppings.append('Grated Reggiano Cheese')

class NYStyleClamPizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'NY Style Clam Pizza'
    self._dough = 'Thin Crust Dough'
    self._sauce = 'Marinara Sauce'
    self._toppings.append('Grated Reggiano Cheese')
    self._toppings.append('Fresh Clams from Long Island Sound')
    
class NYStylePepperoniPizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'NY Style Pepperoni Pizza'
    self._dough = 'Thin Crust Dough'
    self._sauce = 'Marinara Sauce'
    self._toppings.append('Grated Reggiano Cheese')
    self._toppings.append('Sliced Pepperoni')
    self._toppings.append('Garlic')
    self._toppings.append('Onion')
    self._toppings.append('Mushrooms')
    self._toppings.append("Red Pepper")

class NYStyleVeggiePizza(Pizza):    
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'NY Style Veggie Pizza'
    self._dough = 'Thin Crust Dough'
    self._sauce = 'Marinara Sauce'
    self._toppings.append('Grated Reggiano Cheese')
    self._toppings.append('Garlic')
    self._toppings.append('Onion')
    self._toppings.append('Mushrooms')
    self._toppings.append("Red Pepper")
  
class ChicagoStyleCheesePizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'Chicago Style Deep Dish Cheese Pizza'
    self._dough = 'Extra Thick Crust Dough'
    self._sauce = 'Plum Tomato Sauce'
    self._toppings.append('Shredded Mozzarella Cheese')
    
class ChicagoStyleClamPizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'Chicago Style Clam Pizza'
    self._dough = 'Extra Thick Crust Dough'
    self._sauce = 'Plum Tomato Sauce'
    self._toppings.append('Shredded Mozzarella Cheese')
    self._toppings.append('Frozen Clams from Chesapeake Bay')
  
class ChicagoStylePepperoniPizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'Chicago Style Pepperoni Pizza'
    self._dough = 'Extra Thick Crust Dough'
    self._sauce = 'Plum Tomato Sauce'
    self._toppings.append('Shredded Mozzarella Cheese')
    self._toppings.append('Black Olives')
    self._toppings.append('Spinach')
    self._toppings.append('Eggplant')
    self._toppings.append('Sliced Pepperoni')

class ChicagoStyleVeggiePizza(Pizza):
  def __init__(self):
    Pizza.__init__(self)
    self._name = 'Chicago Deep Dish Veggie Pizza'
    self._dough = 'Extra Thick Crust Dough'
    self._sauce = 'Plum Tomato Sauce'
    self._toppings.append('Shredded Mozzarella Cheese')
    self._toppings.append('Black Olives')
    self._toppings.append('Spinach')
    self._toppings.append('Eggplant')
    
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
  
class NYPizzaStore(PizzaStore):
  def __init__(self):
    PizzaStore.__init__(self)
  
  def _createPizza(self, item):
    if item == 'cheese':
      return NYStyleCheesePizza()
    elif item == 'veggie':
      return NYStyleVeggiePizza()
    elif item == 'clam':
      return NYStyleClamPizza()
    elif item == 'pepperoni':
      return NYStylePepperoniPizza()

class ChicagoPizzaStore(PizzaStore):
  def __init__(self):
    PizzaStore.__init__(self)
    
  def _createPizza(self, item):
    if item == 'cheese':
      return ChicagoStyleCheesePizza()
    elif item == 'veggie':
      return ChicagoStyleVeggiePizza()
    elif item == 'clam':
      return ChicagoStyleClamPizza()
    elif item == 'pepperoni':
      return ChicagoStylePepperoniPizza()
    
if __name__ == '__main__':
  nyStore = NYPizzaStore()
  chicagoStore = ChicagoPizzaStore()
  
  pizza = nyStore.orderPizza("cheese")
  print 'Ethan ordered a %s' % pizza.getName()
  
  pizza = chicagoStore.orderPizza("cheese")
  print 'Joel ordered a %s' % pizza.getName()
  
  pizza = nyStore.orderPizza("clam")
  print 'Ethan ordered a %s' % pizza.getName()
  
  pizza = chicagoStore.orderPizza("clam")
  print 'Joel ordered a %s' % pizza.getName()
  
  pizza = nyStore.orderPizza("pepperoni")
  print 'Ethan ordered a %s' % pizza.getName()
  
  pizza = chicagoStore.orderPizza("pepperoni")
  print 'Joel ordered a %s' % pizza.getName()
  
  pizza = nyStore.orderPizza("veggie")
  print 'Ethan ordered a %s' % pizza.getName()
  
  pizza = chicagoStore.orderPizza("veggie")
  print 'Joel ordered a %s' % pizza.getName()
  
  