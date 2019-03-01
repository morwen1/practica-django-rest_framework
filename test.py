
class prueba():
    def metodo():
        a = 2
        return a
    class meta():
        def __init__(self,metodo):
            a = self.metodo()

obj = prueba()
p = obj.meta().a

print(p)
