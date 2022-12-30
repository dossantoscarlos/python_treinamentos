class Saque :
    def __init__(self, saldo:float, saque:float ):
        self.saldo = saldo
        self.saque = saque
        
    def atualizaSaldo (self, saldo:float):
        self.saldo = saldo
        
    def feedbackResultadoSaque(self, saldo_final: float):
        if (saldo_final >= 0 & saldo_final <= self.saldo):    
            self.atualizaSaldo(saldo_final)
            return "Efetuado com sucesso!"     
        return "Saque Invalido!" 
    
    def executaSaque(self) :
        return self.saldo - self.saque; 
        
    def valorDeSaqueMaiorQueZero(self):
        if(self.saque > 0):
            return self.feedbackResultadoSaque(
                self.executaSaque()
            )    
        else:
            return "Saque invalido!"
        
    def sacar(self) :
        return self.valorDeSaqueMaiorQueZero()

