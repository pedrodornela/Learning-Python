tex = 'Curso em Video Python'
##Fatiação
#mostra o elemento do indice digitado(obs: começa semprre do zero)
print(tex[3])

#mostra os elementos entre o range, menos o ultimo
print(tex[3:13])

#mostra do primeiro até uma casa antes do indice
print(tex[:13])

#mostra do indice até o último indice
print(tex[15:])

#mostra os caracteres entre os indice pulando de tantas em tantas casas(ex:2)
print(tex[1:15:2])

#mostra do indice de tantos em tantos caracteres(ex: 1°(indice) -> ::2)
print(tex[::2])

# 3 aspas duplas(no começo e final), quando o texto tem mais de uma linha
##
#mostra o comprimento da frase('tex')
print(len(tex))

#conta quantos elementos iguais possuiem 'tex'
print(tex.count('o'))

#conta quantos elementos iguais possuiem 'tex', com fatiamneto
print(tex.count('o', 0, 13))

#mostra em que momento começa a frase em aspas
print(tex.find('deo'))

#recebe sempre -1, por no ser encontrao
print(tex.find('Android'))

#retorna True se possui dentro de 'tex'
print('curso' in tex)

##TRANFORMAÇÃO

#encontrar e substituir(mas não necessariamente salva
print(tex.replace('python','android'))
#somente se for: tex = tex.replace('python', 'android')


#tornar todo o texto maisculo 'upper', e minusculo 'lower'
print(tex.upper())
print(tex.lower())

#torna somente o primeiro caractere maiusculo, resto fica em minusculo
print(tex.capitalize())

#torna todo começo de frase maiusculo
print(tex.title())

#exclui 'espaços' excedentes no começo e fim, e o indice 1 começa do primeiro caractere
frase = '   Aprenda Python  '
print(frase.strip())

#remove somente espaço excedente da direita
print(frase.rstrip())
#e a esquerda
print(frase.lstrip())

#mostra a quantidade de caracteres repetidos jogados para maiusculo ou minusculo
print(tex.upper().count('O'))

##Divisão
#exclui os '' entre o texto, faz uma lista, toda frase é um indice e todo novo começo de frase o indice começa do 0(nao continua, que nem anteriormente)
print(tex.split())

##Junção
#
print(''.join(tex))