import re
class Students:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def __str__(self):
        return f"{self.name} is from {self.country}"
    def charm(self):
        match self.country:
            case "TANZANIA":
                return f"{self.name} is a Tanzanian"
            case "KENYA":
                return f"{self.name} is a Kenyan"
            case "UGANDA":
                return f"{self.name} is a Ugandan"
            case _:
                return '/'
    # getter
    @property
    def name(self):
        return self._name
    #setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("missing name! ")
        self._name = name
    # getter
    @property
    def country(self):
        return self._country
    # setter
    @country.setter
    def country(self, country):
        if not re.search("kenya|tanzania|uganda", country, re.IGNORECASE):
            raise ValueError("please insert a valid country!")
        self._country = country



# getting name and country and assign them to "Student" class
def students_fn():
    name = input("name: ").rstrip().upper()
    country = input("place: ").upper()
    return Students(name, country)

# the main function (main station or operator)
def main():
    student = students_fn()
    print(student)
    print(student.charm())
    return student

# ensuring main function is only called when needed.
if __name__ == "__main__":
    main()
