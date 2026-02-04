class TeaLeaf():

    def __init__(self,age):
        self._age =age
    

    @property
    def age(self):
        return self._age + 2 
    
    @age.setter
    def age(self, age):
        if age >= 1 and age <= 5:
            self._age = age
        
        else:
            raise ValueError("Tea Leaf age should be in b/w 1 to 5.")
        
            
leaf = TeaLeaf(2)
print(leaf.age)
leaf.age = 6
print(leaf.age)