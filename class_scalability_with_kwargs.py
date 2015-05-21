class Example:
    def __init__(self, **kwargs): # 1 asterisk would mean you want the arg passed in as a tuple, 2 asterisks means you want it passed in as a dict
        self.variables = kwargs
        
    def set_vars(self,k,v):
        self.variables[k] = v
        
    def get_vars(self,k):
        return self.variables.get(k, None)
        
var = Example(Age=17, Location = 'UK')
var.set_vars('name', 'alex')
print(var.get_vars('name'))
print(var.get_vars('Location'))