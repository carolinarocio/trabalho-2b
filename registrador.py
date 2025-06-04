class Registrador:
    def __init__(self, valor=0):
        self.valor = 0 if valor < 0 else valor  # Inicializa o valor do registrador com 0 se o valor passado for negativo

    def incrementar(self):
        self.valor += 1  # Incrementa o valor do registrador

    def decrementar(self):
        if self.esta_zero():  # Se o valor do registrador for zero, não decrementa
            return
        self.valor -= 1  # Decrementa o valor do registrador

    def esta_zero(self):
        return self.valor == 0  # Verifica se o valor do registrador é zero
