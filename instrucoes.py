class Instrucao:
    def __init__(self, rotulo, operacao, registrador, salto, salto_se_nao=None):
        self.rotulo = rotulo
        self.operacao = operacao
        self.registrador = registrador
        self.salto = salto
        self.salto_se_nao = salto_se_nao

    def executar(self, registradores):
        match self.operacao:
            case "ADD":
                registradores[self.registrador].incrementar()  # Se for uma operação de adição, incrementa o valor do registrador
                return self.salto  # Retorna o valor de salto
            case "SUB":
                registradores[self.registrador].decrementar()  # Se for uma operação de subtração, decrementa o valor do registrador
                return self.salto  # Retorna o valor de salto
            case "ZER":
                if registradores[self.registrador].esta_zero():  # Se for uma operação de verificação de zero, verifica se o valor do registrador é zero
                    return self.salto  # Se for zero, retorna o valor de salto
                else:
                    return self.salto_se_nao  # Se não for zero, retorna o valor de salto_se_nao
            case _:
                return None  # Se a operação não for reconhecida, retorna None

    def __str__(self):
        return f"{self.rotulo}: {self.operacao} {self.registrador} {self.salto} {'' if self.salto_se_nao is None else self.salto_se_nao}"
        # Retorna uma string com a instrução
