#  O que é Linguagem de Programação

# ° As linguagens de programação criadas para solucionar
#qualquer tipo de problemas na áreas tecnológicas computacional.

# ° Cada linguagem possui suas particularidades.

# ° Permite que um programador crie programas a partir de um conjuto de ordens,
#ações consecutivas, dados e algoritimos.

# ° Python é uma linguagem de sript de alto nível,
#de tipagem forte e dinamica.

####  História

# ° Criado no início dos anos 1990 por Guido Van Rossum no Stichting
#Mathematisch Centrum (CWI), na Holanda, foi sucessor de uma linguagem chamada ABC.

# ° Em 2001, a Python Software Foundation (PSF) foi formada,
#uma organização sem fins lucrativos criada especificadamente
#para possuir a prosperidade intelectual relacionada ao Python.

 ### PQ PYTHON?

# ° Python é uma linguagem de programação clara e poderosa.

# ° Usa sintaxe clara, facilitando a leitura dos programadores
#que vc escreve;

# ° Linguagem facíl, ideal para o desenvolvimento de protótipos e
#outras tarefas de programação; 

# ° Grande biblioteca padrão, suporta muitas tarefas de programação;

# ° Possui inúmeras bibliotecas que estendem seu poder de atuação. 

# ° Linguagem interpretada, ou seja, uma vez escrito o código, esta
#não precisa ser convertido em linguagem de máquina por um 
#processo de compilação;

# ° Permite atribuição mútipla; 

# ° O interpretador Python 3 utiliza unicode por padrão, o que torna possível 
#usar nomes de váriaveis com acento e até outros caracteres
#especiais, porém não é uma boa prática. 

# ° Códigos em Python pode ser feito em local quanto em nuvem.

###

print("Olá mundo!")

###

### Mais ferramentas

# ° Para implementação de soluções, normalmente utiliza-se uma
#IDE, (Integranted Development Environment) ou Ambiente
# de Desenvolvimento Integrado.

# ° Duas IDE's disputam a preferencia dos desenvolvedores Python,

#°O PyCharm e o Visual Code (VSCode).

     # PyCharm: Profissional e Community, sendo a primeira paga e a 
     # segunda gratuita.
     # VSCode: Gratuito

 ###
  
 #  Variáveis
  
 # ° Variáveis são espaços alocados na memória RAM para guardar
 # valores temporariamente.
 
 # ° Em Python, esses esoaços não precisam ser tipados, a variável
 # pode ser alocada sem especificar o tipo de dado que ela aguardará. 

 # ° As variáveis são tipadas dinamicamente nessa linguagem
 
 #  Veja alguns exemplos:

 # Para saber o tipode dado que uma variável guarda, podemos 
 #imprimir seu tipo usando a função type(), 
 # veja como:     
 
teste4.py>__annotations__
x = 10
nome = "Teste"
nota = 8.5
flag = True

print(type(x))
print(type(nome))
print(type(nota))
print(type(flag))

# Foi criado 4 variáveis diferentes e cada uma dela tem um valor
# o sinal de = é para o seu interpretador entender que esta crinando uma variavel 

# resultato do que foi escrito em cima
# <class `'int'>`
# <class 'str'>
# <class 'float'>
# <class 'bool'>

# tudo seria orientada a objeto!

# Em Python, tudo é OBJETO! Por isso os tipos de dados aparecem com
# a palavra "class".

# Função input() faz a leitura de um valor digitado. 
# Veja como usar:

nome = input("Digite um nome: ")
print(nome)


##

# Temos uma variedade de formas de imprimir texto e variável em Python.

# Vejamos algumas:
  # ° podemos usar formatadores de caracteres (igual em C)
  # ° podemos usar a função format() e
  # ° podemos criar uma string formatada.

  # Modo 1: usando formatadores de caracteres (igual na linguagem C):
print("Olá %s, bem vindo a disciplina de programação. Parabens pelo seu primeiro hello world"%(nome))
# o %s é pq eu quero colocar em uma string, meio que espelhar a palava nome

  # Modulo 2: usando a função format() para imprimir variável e texto:
print("Olá{}, bem vindo a disciplina de programação. Parabéns pelo seu primeiro hello world".format(nome))


  # Modo 3: usando string formatadas
print(f"Olá {nome}, bem vindo a diciplina de programação. Parabéns pelo seu primeiro hello world")


# ° Usamos o hash criar comentários de uma linha. 

# ° Nessa PEP, a 498, o autor destaca o uso do "modo 3" como a 
#mehlor opção, chamndo-a de "f-strings".

# ° As strings formatadas com "f-strings" só podem ser usadas com o 
#interpretador Python na versão 3.6.

###

# Operações matematicas suportadas por Python

# Com exceção das funções abs() e pow() e da notação de potência 
# **, as outras operações e sintaxe são similares a diversas
# linguagens de programação.

# Opetin  |   Result

# x + y       sum of x and y
# x - y       difference of x and y
# x * y       product of x and y 
# x / y       quotient of x and y
# x // y      floored quotient of x and y 
# x % y       remainder of x / y
# - x         x negated 

## abs() ela vai retornar o valor 

 # abs(x)
 # int (x)
 # float (x)
 # complex (re, im)
 # c.conjugate()
 # divnod (x, y)
 # pow (x, y)
 # x ** y

 ## 

 # Repare como é fundamental conhecer a ordem de procedêdencia das 
 #operações para não criar cálculos errados durante a implementação
 #de uma solução.

 # 1. Primeiro resolvem-se os parênteses, do mais interno para o 
 #mais externo.

 # 2. Exponenciação

 # 3. Multiplicação e divisão. 

 # 4. Soma e subtração.

## Exemplo:

#operacao_1 = 2 + 3 * 5  O RESUTADO É 17 / CALCULA 5 X 3 = 15 + 2
#operacao_2 = (2 + 3) * 5  AQUI SERÁ CALCULADO PRIMEIRO O QUE ESTA DENTRO DOS() resutado 25 
##operacao_3 = 4 / 2 ** 2   // resultado 1.0
#operacao_4 = 13 % 3 + 4   // resultado 5

