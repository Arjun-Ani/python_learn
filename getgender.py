class person(object):
    def __init__(self,name):
        self.name=name
    def male(self):
        return self.name+" is male"
    def female(self):
        return self.name+" is female"

a=person("arjun")
print a.male()


