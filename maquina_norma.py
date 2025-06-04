import re
from instrucoes import Instrucao
from registrador import Registrador

class MaquinaNorma:
    def __init__(self):
        self.registradores = {chr(65 + i): Registrador() for i in range(8)}  # Dicionário com registradores de A-H
        self.programa = {}  # Dicionário com as instruções do programa carregado
        self.ponteiro = 1  # Ponteiro para a próxima instrução

    def carregar_programa(self, nome_arquivo):
        self.programa = {}  # Limpa o dicionário de instruções
        with open(nome_arquivo, "r") as arquivo:
            padrao_instrucao = r"^(\d+):\s*([A-Z]{3})\s*([A-H])\s*(\d+)\s*(\d+)?$"  # Padrão REGEX para identificar instruções no arquivo
            instrucoes = re.findall(padrao_instrucao, arquivo.read(), re.MULTILINE)  # Lista de instruções no arquivo

            for instr in instrucoes:
                rotulo, operacao, registrador, salto, salto_se_nao = instr  # Desempacotamento dos grupos capturados

                rotulo = int(rotulo)      # Converte o rótulo para inteiro
                salto = int(salto)        # Converte o salto para inteiro
                salto_se_nao = int(salto_se_nao) if salto_se_nao and salto_se_nao.strip() else None  # Converte o salto_se_nao para inteiro, se existir

                self.programa[rotulo] = Instrucao(rotulo, operacao, registrador, salto, salto_se_nao)  # Adiciona a instrução ao dicionário

    def inicializar_registradores(self, valores):
        for r in self.registradores:  # Percorre todos os registradores
            if r in valores:
                self.registradores[r].value = valores[r]  # Se existir valor para o registrador, atribui o valor
            else:
                self.registradores[r].value = None  # Se não existir valor para o registrador, atribui None

    def executar(self):
        print(self)

        while self.ponteiro is not None:
            if self.ponteiro not in self.programa:
                break

            self.ponteiro = self.programa[self.ponteiro].execute(self.registradores)
            print(self)

    def __str__(self):
        regs = {r: self.registradores[r].value for r in self.registradores if self.registradores[r].value is not None}
        return f"Registradores: {regs} | Ponteiro: {self.ponteiro} | Instrução: {self.programa[self.ponteiro] if self.ponteiro in self.programa else None}"  # Retorna uma string com os registradores, ponteiro e instrução atual
