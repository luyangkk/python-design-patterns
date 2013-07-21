'''
Created on 2013-2-19

@author: luyangkk
'''

class FlyBehavior:
  '''
    Interface: FlyBehavior 
  '''
  def __init__(self):
    pass
  
  def fly(self, args):
    pass

class FlyWithWings(FlyBehavior):
  def __init__(self):
    FlyBehavior.__init__(self)
  
  def fly(self, args):
    print 'I\'m flying with %s!!' % args[0]

class FlyNoWay(FlyBehavior):
  def __init__(self):
    FlyBehavior.__init__(self)
  
  def fly(self, args):
    print 'I can\'t fly'

class Duck:
  def __init__(self, flyBehavior):
    self.__flyBehavior = flyBehavior
  
  def performFly(self):
    self.__flyBehavior.fly(['wings'])
  
  def setFlyBehavior(self, flyBehavior):
    self.__flyBehavior = flyBehavior
  
class MallardDuck(Duck):
  def __init__(self, flyBehavior):
    Duck.__init__(self, flyBehavior)
    
if __name__ == '__main__':
  flyBehavior = FlyWithWings()
  mallard = MallardDuck(flyBehavior)
  mallard.performFly()
  
  mallard.setFlyBehavior(FlyNoWay())
  mallard.performFly()
  