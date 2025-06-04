import re
from instrucoes import Instrucao
from registrador import Registrador

class MaquinaNorma:
    def __init__(self):
        # cria 8 registradores nomeados de A a H
        self.registradores = {chr(65 + i): Registrador() for i in range(8)}
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
        """Inicializa os registradores conforme o dicionário passado."""
        for r in self.registradores:
            self.registradores[r].valor = valores.get(r, 0)

    def executar(self):
        print(self)

        while self.ponteiro is not None:
            if self.ponteiro not in self.programa:
                break

            # executa a instrução apontada e atualiza o ponteiro
            self.ponteiro = self.programa[self.ponteiro].executar(self.registradores)
            print(self)

    def __str__(self):
        regs = {r: self.registradores[r].valor for r in self.registradores if self.registradores[r].valor is not None}
        return f"Registradores: {regs} | Ponteiro: {self.ponteiro} | Instrução: {self.programa[self.ponteiro] if self.ponteiro in self.programa else None}"  # Retorna uma string com os registradores, ponteiro e instrução atual
