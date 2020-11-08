import random

def init():
    #Adjectifs en i
    adji = dict([
        ("おおきい", "grand"),
        ("ちいさい", "petit"),
        ("ながい", "long"),
        ("みじかい", "court"),
        ("あつい", "chaud (climat)"),
        ("さむい", "froid (climat)"),
        ("あつい", "chaud (objet)"),
        ("つめたい", "frais (objet)"),
        ("たかい", "haut"),
        ("ひくい", "bas"),
        ("たかい", "cher"),
        ("やすい", "bon marché"),
        ("むずかしい", "difficile"),
        ("やさしい", "facile"),
        ("あたらしい", "nouveau/neuf"),
        ("ふるい", "vieux/ancien"),
        ("おもしろい", "intéressant"),
        ("つまらたい", "ennuyeux"),
        ("おもい", "lourd"),
        ("かるい", "léger"),
        ("はやい", "rapide/tôt"),
        ("おそい", "long/tard"),
        ("おいしい", "délicieux/bon"),
        ("まずい", "mauvais/fade"),
        ("いい", "bon (général)"),
        ("わるい", "mauvais (général)"),
        ("いそがしい", "occupé"),
        ("じゆう", "libre")
    ])

    #Verbe
    verbe = dict([
        ("todo","todo")
    ])

    return adji, verbe

def exadji(adji, langue):
    liste  = []
    if (langue == "jap"):
        liste = list(adji.keys())
    elif (langue == "fr"):
        liste = list(adji.values())
    elif (langue == "deux"):
        liste = list(adji.keys()) + list(adji.values())
        
    print("Donne la traduction de chaque mots : ")
    print("Tips : Si t'as besoin d'écrire en hiragana il y a ce site : https://www.lexilogos.com/keyboard/hiragana.htm ")
    for i in range (random.randrange((len(liste)//2), len(liste))):
        mot = liste[random.randrange(0, len(liste))]
        print(mot)
        trad = input ("traduction : ")
        if (trad != mot): 
            print("Non ! C'était "+ str(adji.setdefault(mot)))


    

    return None

def exverbe(list, langue):
    #todo
    return 1


def main():

    #Init des listes de mots
    adji, verbe = init()
    
    while (1):
        print("Pour faire un choix, écris un des mots entre ''")
        choix = input(" 'adji' ou 'verbe' ou on 'stop' ? \n")
        if (choix == "stop"): break
        langue = input("en 'jap', 'fr' ou les 'deux' ? \n")

        if (choix == "adji"):
            exadji(adji, langue)
        elif (choix == "verbe"):
            exverbe(verbe, langue)
        else:
            print("J'ai pas compris tes choix frère")

        print("-------------------------------------------------")

    return None


if __name__ == '__main__':
    main()
    