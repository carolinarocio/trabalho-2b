from maquina_norma import MaquinaNorma

def principal():
    testar_mod(5, 15)

def adicionar_dois_numeros(a, b):
    maquinaNorma = MaquinaNorma()

    maquinaNorma.carregar_programa("./operations/add_two_numbers.txt")
    maquinaNorma.inicializar_registradores({ 'A': a, 'B': b, 'C': 0 })

    maquinaNorma.executar()

def multiplicar_dois_numeros(a, b):
    maquinaNorma = MaquinaNorma()

    maquinaNorma.carregar_programa("./operations/multiply_two_numbers.txt")
    maquinaNorma.inicializar_registradores({ 'A': a, 'B': b, 'C': 0, 'D': 0 })

    maquinaNorma.executar()

def fatorial(n):
    maquinaNorma = MaquinaNorma()

    maquinaNorma.carregar_programa("./operations/factorial.txt")
    maquinaNorma.inicializar_registradores({ 'A': n, 'B': 0, 'C': 0, 'D': 0 })

    maquinaNorma.executar()

def verificar_se_um_e_menor_que_outro(a, b):
    maquinaNorma = MaquinaNorma()

    maquinaNorma.carregar_programa("./operations/a_less_than_b.txt")
    maquinaNorma.inicializar_registradores({ 'A': a, 'B': b, 'C': 0, 'D': 0, 'E': 0 })

    maquinaNorma.executar()

def testar_mod(a, b):
    maquinaNorma = MaquinaNorma()

    maquinaNorma.carregar_programa("./operations/test_mod_a_b.txt")
    maquinaNorma.inicializar_registradores({ 'A': a, 'B': b, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0 })

    maquinaNorma.executar()

def testar_primo(a):
    maquinaNorma = MaquinaNorma()

    maquinaNorma.carregar_programa("./operations/test_primo_a.txt")
    maquinaNorma.inicializar_registradores({ 'A': a })

    maquinaNorma.executar()

if __name__ == "__main__":
    principal()
