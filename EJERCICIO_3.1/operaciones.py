from re import A


class operaciones:
    """Clase con las operaciones básicas
        """
    
    def __init__ (self,a,b):
        self.a = a
        self.b = b

    def suma (self):
        """Realiza una suma a partir de dos numeros pasados
        """
        return self.a+self.b

    def resta (self):
        """Realiza una resta a partir de dos numeros pasados
        """
        return self.a-self.b

    def multiplicacion (self):
        """Realiza una multiplicación a partir de dos numeros pasados
        """
        return self.a*self.b

    def division (self):
        """Realiza una division a partir de dos numeros pasados
        """
        return self.a/self.b

