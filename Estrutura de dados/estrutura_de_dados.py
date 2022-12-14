# -*- coding: utf-8 -*-
"""Book Estrutura de dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/175Sp4HlLjz6D5U7_4Suq0Z3esuoGzSb1

Revisão de conteúdo sobre o livro <b>Python para Análise de Dados</b> do autor Wes Mckinney .

By: Rogério Sobral Ribeiro

<b>Fonte: MCKINNEY,Wes. Python para Análise de Dados. São Paulo. O.Reilly- Novatec .2018</b>

#Estruturas de dados Embutidas

Vamos nessa discussão refletir as Collections, sabemos que no dia a dia utilizaremos bibliotecas com Pandas e Numpy para trabalhar com conjunto de dados maiores, porém precisaremos utilizar em conjunto com as estruturas Embutidas.

##Tuplas
Caracteristicas:
* Imutável
* Tamanho Fixo

###Criando Tuplas
Para cria-las deve-se colocar os valores separados por virgulas
"""

tup=2,3,4
tup

"""<b>Obs:</b> Repare que quando é solicitado a sua impressão na tela, temos os valores dentro de parenteses.

Podemos ainda criar tuplas de outras maneiras

"""

tup=(1,2,3,4,5)
tup

"""Podemos criar tuplas alinhadas, no qual futuramente veremos como acessar seus valores"""

nested_tup=(4,5,6,7),(2,3,4)
nested_tup

"""###Convertendo um arquivo em uma Tupla
Para converter uma outra collection em uma tupla basta
"""

dic=[2,3,4,5]
tup=tuple(dic)
print(tup)
#ou 
tup=tuple([2,3,4,5])
print(tup)

"""###Acessando dados em uma Tupla
Para acessar usamos [  ] e o valor do indice dentro,Exemplo: 

<b>indice:  0, 1, 2, 3, 4

  tupla= ('a','b','c','d')</b>

Veja que para cada elemento na Tupla existe um indice, esse correspondendo ao endereço da informação.
"""

tupla= ('a','b','c','d')
tupla[0],tupla[1],tupla[2],tupla[3]

tupla[1:3]

"""###Desempacotamento de tuplas"""

tupla= ('Carlos','marco','joão')
a,b,c=tupla
a

"""Um uso de tuplas comum é com nested(alinhados)"""

nested_tup=(4,5,6,7),(2,3,4)

a,b=nested_tup
a

a,b,*arg=1,2,3,4,5,6,7,8,9
print(a)
print(b)
print(arg)

"""Por causa da não mutabilidade da tupla, ela possui poucos metodos."""

tup=1,2,3,4,5,6,7,8,9
tup.count(2) # Conta as ocorrências do valor

tup.index(2) #Retorna o index do valor

"""##Lista
Caracteristica:
* Mutável in-place
* Tamanho variavel

###Criando uma lista
"""

lista=["Carlos", "Marcos", "Pedro"]
lista=["Carlos", "Marcos", "Pedro",1,2,True]
lista

"""Espressão Geradora"""

lista=range(10)
lista # range(0, 10)
list(lista)

"""###Adicionando e removendo elementos"""

lista=[]
lista.append("Suzano")

lista.append("salvador")
lista

"""O metodos insert é custoso no processamento, pois tem que percorrer a collection e depois reorganiza-lá """

lista.insert(1,"São Paulo")
lista

"""###Deletando dados da Lista

O metodo POP retorna o valor do index e depois deleta-o.
"""

lista=["Carlos", "Marcos", "Pedro",1,2,True]
nome=lista.pop(0)

nome

"""O metodo deleta os valores"""

lista.remove("Marcos")

lista

"""Pode-se utilizar a palavra  reservada "in" para verificar se existe algum elemento na lista"""

lista=["Carlos", "Marcos", "Pedro",1,2,True]

print("Carlos" in lista)

# ou pode-se usar a palavra reservada "not" para negar
print("Carlos" not in lista)

"""###Concatenando e combinando lista

É preferivel usar "extend" do que adição(+) pois é menos custoso em aspecto de processamento
"""

[4,5,6,7,8,9]+[5,6,7,82,"Carlos"]

lista=[4,5,6,7,8,9]
lista2=["Carlos", "pedro"," João"]
lista.extend(lista2)
lista

"""###Ordenação"""

numeros=[4,6,8,1,3,2,7]
numeros.sort() #ordena
numeros.sort(reverse=True) #Ordena Invertido
numeros

nomes=["Carlos", "pedro"," João"]
nomes.sort(key=len)#Ordena por tamanho
nomes

"""###Busca Binaria e manutenção de uma lista

Podemos inseir um valor na lista seguindo sua ordenação usando "bisect.insort"

"""

import bisect

co=[1,2,2,3,4,5,6]
bisect.bisect(co,3) ## encontra o local do valor

c

bisect.insort(co,2) #insere o valor na posição segundo a ordenação
co

"""###Fatiamento

Podemos selecionar porção de uma lista usando o conceito de (slice) passando um [start:stop]
"""

numeros=[1,2,3,4,5,6,7]
numeros[2:7]

"""Faça seus testes colocando valores dentro do range do index.

Você pode selecionar realizando o fatiamento em relação ao final.
"""

numeros=[1,2,3,4,5,6,7]
numeros[-4:]

"""###Sorted

Devolve uma nova lista Ordenada
"""

numeros=[1,2,3,4,5,6,7]
sorted(numeros)
numeros

"""###ZIP
Esse metodo Parei listas e tuplas e outras collections
"""

nome=["Carlos", "pedro"," João"]
sobrenome=["Rocha", "Silva"," Lucio"]
zipped=zip(nome,sobrenome)
list(zipped)

"""###Reversed
Itera na ordem inversa
"""

list(reversed(range(10)))

"""##Dict

Essa pode ser vista como uma das estruturas de dados embutidas  mais importante.
Ela trabalha com a ideia de {Chave: valor}.
Usa-se dois ":" para separar chaves do valor

Caracteristica:

* Mutável in-place
* Tamanho flexivel

###Criando Dict
"""

empty_dict={}

#            Key:   Value
empty_dict["nome"]="Rogerio"
empty_dict

d1={"a":"some value","b":"other value"}
d1

"""Pode-se utilizar numeros como key."""

d2={}
d2[1]="one register"
d2

"""Pode-se salvar outras estruturas embutidas como "Values"."""

register={"Nomes":['Carlos','marco','joão'],"Idades":[18,12,63]}
register

"""Um dos usos que temos para dicionários, é para trabalhar criando DataFrames com pandas, observe o exemplo abaixo:"""

import pandas as pd

pd.DataFrame(register)

"""Para verificar se um dicionário possui uma chave é com a palavra reservada IN"""

"Nomes" in register 
# lembrando a palavra deve estar escrita perfeitamente igual a da key

"""###Apagando"""

register={"Nomes":['Carlos','marco','joão'],"Idades":[18,12,63]}

del register["Idades"]
register

del register["Nomes"][0] # o segundo colchetes serve para definir qual valor
register

"""O método "pop" funciona da mesma maneira que o list.
Porem ele buscar através da Key/chave e retorna os values.
"""

register={"Nomes":['Carlos','marco','joão'],"Idades":[18,12,63]}

elemento=register.pop("Nomes")
elemento

"""Criando um programa de perguntas"""

questionario={"Pergunta 1":{"Pergunta":"Qual a media de 5,5,5",
                            "Respostas":{"a":"5","b":"4","c":"10","d":"15"},
                            "Resposta Certa":"a"
                           },
              "Pergunta 2":{"Pergunta":"Quanto é 2 + 2",
                            "Respostas":{"a":"5","b":"4","c":"10","d":"15"},
                            "Resposta Certa":"b"
                           },
              "Pergunta 3":{"Pergunta":"Quanto é 2 - 2",
                            "Respostas":{"a":"5","b":"4","c":"0","d":"15"},
                            "Resposta Certa":"c"
                           },
             }

for ky,vl in questionario.items():
  print(f'{ky} = {vl["Pergunta"]}')
  
  for ky2,vl2 in vl["Respostas"].items():
    print(f'{ky2} = {vl2}')
  resposta=input("Resposta")
  if vl["Resposta Certa"]==resposta:
    print(f"Você acertou a ")

"""###Interador de Keys e Values
Podemos pegar a chave ou os valores de um dicionário diretamente, os percorrendo.
"""

register={"Nomes":['Carlos','marco','joão'],"Idades":[18,12,63]}

register.keys()

register.values()

"""###Combinando Dicionários

Podemos combina-los usando o metodo "update"
"""

register={"Nomes":['Carlos','marco','joão'],"Idades":[18,12,63]}

phone={"phone_number":["11 9 89098857","11 9 55555555","11 9 333333333"]}

register.update(phone)
register

"""###Criando dicionários a partir de sequências"""

keys=[1,2,3]
values_nomes=['Carlos','marco','joão']
register=dict(zip(keys,values_nomes))
register

"""###Valores Default"""

default_value=""
for key in register:
  value=register[key]
  print(value)
else:
  value=default_value

"""O mesmo codigo acima pode ser escrito da seguinte maneira"""

register={"Nomes":['Carlos','marco','joão'],"Idades":[18,12,63]}
value=register.get("Nomes","Nan")
value

"""Vamos criar um classificador por letras/letter.
Lembrando todas as letras estão minusculas.
Presta muita atenção neste códico:
"""

words=["carro", "mala", "peso",
       "macaco", "coisas","abobora",
       "jarro","amazonas"]
by_letter={}

for word in words:
  letter=word[0]# retorna a primeira letra

  if letter not in by_letter:

    by_letter[letter]=[word]

  else:
    by_letter[letter].append(word)


by_letter

by_letter={}
for word in words:
  letter=word[0]
  by_letter.setdefault(letter,[]).append(word)

by_letter

"""###Tipos de chaves válidas para dicionários

As chaves devem ser sempre objetos imutáveis, como os tipos escalares(int, float, string), tuplas tambem são. 

O termo técnico é hashability(possibilidade de hashing) 
para verificar usa-se o hash
"""

hash("string")

hash(("string","string2"))



hash(2)

try:
  hash([23,34])
 # neste caso ele lança um erro, pois é mutavel,
 # hashability
except Exception as f:
  print(f"invalid syntax {f}")

"""##SET

Collection não ordenada e elementos únicos.

* Mutável
* Tamanho flexivel
* Não aceita repteções

###Criando um SET
"""

conjunto=set([2,2,4,5,67,8,2])
conjunto

"""Repare que temos a aparição de 3 valores "2", mas quando criamos o set e mandamos imprimir na tela só nos retorna 1, pois ele não repete valores."""

conjunto2={2,3,4,5,6,6,8,9}
conjunto2

"""###União de conjutos"""

a={2,3,4,5,6}
b={6,8,9}
a.union(b) # o 6 não foi repetido
#ou
a|b

"""###Intersecção  de conjuntos"""

a={2,3,4,5,6}
b={6,8,9}
a.intersection(b)# somente o 6 esta nos dois conjuntos
a&b

"""###Lista de métodos"""

#Add  Adicionar

a.add(10)
a

#clear  limpar
print(b)
b.clear()
print(b)

#remove  remeove um item 
a.remove(10)
a

#pop  apaga um elemento arbitrariamente e retorna ele 
a.pop()

#update  define o conteúdo de "a" como a união dos elementos em "a" e "b"
a={2,3,4,5,6}
b={6,8,9}
a.update(b)
a

#Intersection_update  define o conteúdo de "a" como a intersecção dos elementos em "a" e "b"
a={2,3,4,5,6,8}
b={6,8,9}
a.intersection_update(b)
a

#difference   Os elementos que em "a" que não estão em "b"
a={2,3,4,5,6,8}
b={6,8,9}
a.difference(b)

#difference_update   Define "a" com os elementos que estão em  "a"  e que não estão em "b"
a={2,3,4,5,6,8}
b={6,8,9}
a.difference_update(b)
a

#symmetric_difference  todos elementos que estão em "a" ou em "b" mas não em ambos
a={2,3,4,5,6,8}
b={6,8,9}
a.symmetric_difference(b)

#symmetric_difference_update  define "a" com todos elementos que estão em "a" ou em "b" mas não em ambos
a={2,3,4,5,6,8}
b={6,8,9}
a.symmetric_difference_update(b)
a

# issubset retorna True se "a" estiver todo contido em  "b"
a={2,3,4,5,6,8}
b={6,8,9}
print(b.issubset(a))

c={5,6,8}
print(c.issubset(a)) # c esta contido em a?