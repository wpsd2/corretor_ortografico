import nltk as nltk

with open("files/artigos.txt", "r", encoding="utf8") as f:
    artigos = f.read()
# print(artigos[:500])


texto_exemplo = "Olá, tudo bem?"
palavras_separadas = texto_exemplo.split()

# print(palavras_separadas)
# print(len(palavras_separadas))

texto_exemplo = "Olá, tudo bem?"
tokens = texto_exemplo.split()
# print(len(tokens))
# print(tokens)

# nltk.download('punkt')
palavras_separadas = nltk.tokenize.word_tokenize(texto_exemplo)
# print(palavras_separadas)



def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)
    return lista_palavras


# print(separa_palavras(palavras_separadas))


lista_tokens = nltk.tokenize.word_tokenize(artigos)
lista_palavras = separa_palavras(lista_tokens)
# print(f"O número de palavras é: {len(lista_palavras)}")

# print(lista_palavras[:5])


def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada

lista_normalizada = normalizacao(lista_palavras)
# print(lista_normalizada[:5])


len(set(lista_normalizada))


lista = "lgica"
(lista[:1], lista[1:])
palavra_exemplo = 'lgica'



palavra_exemplo = "lgica"

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras


def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    return palavras_geradas

palavras_geradas = gerador_palavras(palavra_exemplo)
# print(palavras_geradas)


def corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    palavra_correta = max(palavras_geradas, key=probabilidade)
    return palavra_correta


frequencia = nltk.FreqDist(lista_normalizada)
total_palavras = len(lista_normalizada)


def probabilidade(palavra_gerada):
    return frequencia[palavra_gerada]/total_palavras

probabilidade("lógica")
# print(probabilidade("lógica"))



corretor(palavra_exemplo)
# print(corretor(palavra_exemplo))


def cria_dados_teste(nome_arquivo):
    lista_palavras_teste = []
    f = open('files/palavras.txt', "r", encoding='utf-8')
    for linha in f:
        correta, errada = linha.split()
        lista_palavras_teste.append((correta, errada))
    f.close()
    return lista_palavras_teste

lista_teste = cria_dados_teste("palavras.txt")
# print(lista_teste)



def avaliador (testes):
    numero_palavras = len(testes)
    acertou = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = round(acertou*100/numero_palavras, 2)
    print(f"{taxa_acerto}% de {numero_palavras} palavras")

#avaliador(lista_teste)



def deletando_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras


def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)
    return palavras_geradas
palavra_exemplo = "lóigica"
palavras_geradas = gerador_palavras(palavra_exemplo)
# print(palavras_geradas)

#avaliador(lista_teste)


def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras


def deletando_caracteres(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras


def troca_letra(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzáàãâéèêíìóòõôúùûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:])
    return novas_palavras


def inverte_letra(fatias):
    novas_palavras = []
    for E, D in fatias:
        if len(D) > 1:
            novas_palavras.append(E + D[1] + D[0] + D[2:])
    return novas_palavras


def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    palavras_geradas += deletando_caracteres(fatias)
    palavras_geradas += troca_letra(fatias)
    palavras_geradas += inverte_letra(fatias)
    return palavras_geradas


palavra_exemplo = "lgóica"
#palavras_geradas = gerador_palavras(palavra_exemplo)
# print(palavras_geradas)


#avaliador(lista_teste)


def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        if palavra_corrigida == correta:
            acertou += 1
        else:
            desconhecida += (correta not in vocabulario)
    taxa_acerto = round(acertou*100/numero_palavras, 2)
    taxa_desconhecida = round(desconhecida*100/numero_palavras, 2)
    print(f"{taxa_acerto}% de {numero_palavras} palavras, desconhecidas é {taxa_desconhecida}%")


vocabulario = set(lista_normalizada)
avaliador(lista_teste, vocabulario)


palavra = "lóiigica"

def gerador_turbinado(palavras_geradas):
    novas_palavras = []
    for palavra in palavras_geradas:
        novas_palavras += gerador_palavras(palavra)
    return novas_palavras

palavras_g = gerador_turbinado(gerador_palavras(palavra))
"lógica" in palavras_g
#print(len(palavras_g))


def novo_corretor(palavra):
    palavras_geradas = gerador_palavras(palavra)
    palavras_turbinado = gerador_turbinado(palavras_geradas)
    todas_palavras = set(palavras_geradas + palavras_turbinado)
    candidatos = [palavra]
    for palavra in todas_palavras:
        if palavra in vocabulario:
            candidatos.append(palavra)
    palavra_correta = max(candidatos, key=probabilidade)
    return palavra_correta

#print(novo_corretor(palavra))



def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = novo_corretor(errada)
        desconhecida += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = round(acertou*100/numero_palavras, 2)
    taxa_desconhecida = round(desconhecida*100/numero_palavras, 2)
    print(f"{taxa_acerto}% de {numero_palavras} palavras, desconhecidas {taxa_desconhecida}%")



vocabulario = set(lista_normalizada)
avaliador(lista_teste, vocabulario)



def avaliador(testes, vocabulario):
    numero_palavras = len(testes)
    acertou = 0
    desconhecida = 0
    for correta, errada in testes:
        palavra_corrigida = corretor(errada)
        desconhecida += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertou += 1
    taxa_acerto = round(acertou*100/numero_palavras, 2)
    taxa_desconhecida = round(desconhecida*100/numero_palavras, 2)
    print(f"{taxa_acerto}% de {numero_palavras} palavras, desconhecidas {taxa_desconhecida}%")



vocabulario =  set(lista_normalizada)
avaliador(lista_teste, vocabulario)



palavra = "lgica"
print(novo_corretor(palavra))
print(corretor(palavra))

