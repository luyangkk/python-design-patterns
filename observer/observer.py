'''
Created on 2013-3-11

@author: luyang
'''

class Subject:
  '''
    Interface: Subject 
  '''
  def registerObserver(self, o):
    pass
  
  def removeObserver(self, o):
    pass
  
  def notifyObservers(self):
    pass
  
class Observer:
  '''
    Interface: Observer
  '''
  def update(self, temperature, humidity, pressure):
    pass

class DisplayElement():
  '''
    Interface: DisplayElement
  '''
  def display(self):
    pass
  
class WeatherData(Subject):
  def __init__(self):
    self.__observers = []
    self.__temperature = 0.0
    self.__humidity = 0.0
    self.__pressure = 0.0
    
  def registerObserver(self, o):
    self.__observers.append(o)

  def removeObserver(self, o):
    self.__observers.remove(o)
    
  def notifyObservers(self):
    for o in self.__observers:
      o.update(self.__temperature, self.__humidity, self.__pressure)
      
  def measurementsChanged(self):
    self.notifyObservers()
    
  def setMeasurements(self, temperature, humidity, pressure):
    self.__temperature = temperature
    self.__humidity = humidity
    self.__pressure = pressure
    self.measurementsChanged()
    
class CurrentConditionsDisplay(Observer, DisplayElement):
  def __init__(self, weatherData):
    self.__temperature = 0.0
    self.__humidity = 0.0
    self.__weatherData = weatherData
    self.__weatherData.registerObserver(self)
    
  def update(self, temperature, humidity, pressure):
    self.__temperature = temperature
    self.__humidity = humidity
    self.display()
    
  def display(self):
    print 'Current conditions: %.2fF degrees and %s%% humidity' % \
        (self.__temperature, self.__humidity)
        
class ForecastDisplay(Observer, DisplayElement):
  def __init__(self, weatherData):
    self.__currentPressure = 29.92
    self.__lastPressure = 0.0
    self.__weatherData = weatherData
    self.__weatherData.registerObserver(self)
    
  def update(self, temperature, humidity, pressure):
    self.__lastPressure = self.__currentPressure
    self.__currentPressure = pressure
    self.display()
    
  def display(self):
    print 'Forecast:',
    if self.__currentPressure > self.__lastPressure:
      print 'Improving weather on the way!'
    elif self.__currentPressure == self.__lastPressure:
      print 'More of the same'
    else:
      print 'Watch out for cooler, rainy weather'
      
if __name__ == '__main__':
  weatherData = WeatherData()
  currentDisplay = CurrentConditionsDisplay(weatherData)
  forecastDisplay = ForecastDisplay(weatherData)
  weatherData.setMeasurements(80, 65, 30.4)
  weatherData.setMeasurements(82, 70, 29.2)
  weatherData.setMeasurements(78, 90, 29.2)
  
  print '\nbefore remove:'
  weatherData.notifyObservers()
  weatherData.removeObserver(forecastDisplay)
  
  print '\nafter remove:'
  weatherData.notifyObservers()
  
  