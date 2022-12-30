class Deposito :
    def __init__(self,deposito:float, saldo:float): 
        self.deposito = deposito
        self.saldo = saldo
        
    def atualizaSaldoDeposito(self,saldo):
        self.saldo = saldo 
        
    # deposito
    def feedbackResultadoDeposito(self) :
        if(self.deposito > 0):
            self.atualizaSaldoDeposito(self.executaDeposito())  
            return "Deposito realizado com sucesso!"
        return "Deposito não realizado!"
         
    #executando movimentacao    
    def executaDeposito (self) : 
        return self.deposito + self.saldo
            
    #deposito
    def depositar(self) : 
        return self.feedbackResultadoDeposito()
        
        # return "Error ao depositar. Valor invalido!"
            