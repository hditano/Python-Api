import requests

class Person: 
    

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def GetData(self, city):
        api_url = f'http://api.weatherapi.com/v1/current.json?key=59702037ba85410da5e214247230407&q={city}&aqi=no'
        response = requests.get(api_url)
        results = response.json()
        for k,v in results.items():
            print(k, v)
    
    def SpecificData(self):
        userInput = input('Please type a City: ')
        self.GetData(userInput)
        

myPerson = Person('Hernan', 'Di Tano')
print(myPerson.SpecificData())
