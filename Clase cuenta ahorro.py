
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial 

    def consultar_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("Monto inválido")


class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, interes_anual):
        
        super().__init__(titular, saldo_inicial)
        self.__interes_anual = interes_anual 

    def consultar_interes(self):
        return self.__interes_anual

    
    def aplicar_interes(self):
        
        interes_generado = self.consultar_saldo() * (self.__interes_anual / 100)
        
        self.depositar(interes_generado)
        print(f"Interés aplicado: +${interes_generado}")