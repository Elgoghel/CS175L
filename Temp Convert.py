#Marwan Elgoghel
#CS-175L
#Temp Conv
def main():
  controlLoop()

def convertToKelvin():
  global kelvin
  kelvin = (fahrenheit - 32) * 5/9 + 273.15
  return kelvin

def convertToCentigrade():
  global centigrade 
  centigrade = (fahrenheit - 32) * 5/9
  return centigrade

def doConversion():
  getFahrenheit()
  convertToKelvin()
  convertToCentigrade()
  print(f' Fahrenheit: {fahrenheit:.2f} Kelvin: {kelvin:.2f} Centigrade: {centigrade:.2f}')

def repeat():
  howMany = int(input("How many conversions would you like to do this time?: "))
  for x in range (howMany):
      doConversion()

def controlLoop():
  response = input ('Do you want to do some conversions(yes or no)?: ')
  if response.lower() == "yes":
    repeat()

def getFahrenheit():
  global fahrenheit
  fahrenheit = int(input('Enter Fahrenheit temperature (must be -50 to 130): '))
  if fahrenheit < -50 or fahrenheit > 130:
    fahrenheit = int(input("Please enter a valid temperature: "))
  return fahrenheit
  
if __name__ == '__main__':
  main()