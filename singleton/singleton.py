'''
Created on 2013-3-16

@author: luyang
'''

class Singleton:
  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
    return cls._instance