Pour tester, vocabulaire: All, Voc7 (3), p45(1)

Reprise: 
-ligne 204 sorted 
- Si Tilio fait 3x enter sans entrer de text. Il faut compter comme un mot inconnu et pas écrit faux. 
- Simplifier le mecanisme de base, passer vers un mode ou l on doit simplement avoir une question et une réponse. Dans la réponse_donnée on affiche éventuellement une explication plus complète (e.g. <der> Kuchen) . Se débarasser du der, die, das en construisant un dict question réponse comme un autre.

- Faire un fichier de statistic pour le consuleter et fabriquer un nouveau voc des mots difficiles. 
    - On y inscrit le ID et la fréquence d erreur de tous les mots (0 si jamais fait faux). 
    - Le rendre lisible, on y ajoute toutes les informations mais la référence reste le vocabulaire de base
        - On doit pouvoir reconstruire un voc en choisissant une date. Le users se voit offrir un choix de date à laquelle il a fait des exercices (décroissant).
    - Faire un seul fichier avec toutes les stat (Tilio ou autre personne), ne pas multiplier les fichiers
    - Information: Date de la statistque (de l'exercice), Type d exercice (mot - mot der,die,das - phrase etc.)
- Lors de la saisie du voc. Pour copie coller en D. On pourrait vérifier qu'il n'y a que les caractères autorisé (a-z, 1.9 etc. ) pour enlever les "ạ"
- Passer à un system avec un ID unique pour tous les termes.
- le compte 24/25 mots est faut, voir un screenshot de Tilio sur son PC
ecrire ne pas montrer / effacer les lignes précédente sinon on peut facilement copier...
- Tester avec EN, ALL (trouver et écrire)
- Tricherie sans tapper le texte. Empécher l'emploi de la fleche haut pour aller cherher un text dans la memoire tampon.
- enregistrer les mots difficile.
  
Améliorations:
- Lorsqu on doit trouver les motes correspondants: on devrait boucler sur les mots marqués "je ne me souviens pas"
- dans le "trouver" on boucle jusqu'à ce que l on fasse juste du premier coup. S il y a une faute on garde le mot dans la liste et on repose la question. Ce mot est ajouté à la liste de mot difficile, à la fin on pondere selon le nombre de fois ou le mot a été faux.
- Dans le "trouver" on doit associer le mot et les conjugaisons (e.g. kennen|lernen)
- aller du FR et trouver all est plus dif. pour Tilio
    Verbes:
        Distinguer les verbes des phrases
        DIstinguer les verbes infinitif des verbes conjgués.
- Ajouter une version dans l entete
- Afficher une seule ligne en haut avec tout les choix qui ont été choisi au démarrage.
Se passer de la conversion .csv vers JSON
 
en cours:
    - Gestion de l'effort, temps de sprint - Reprendre ligne 143 "exercice1.addChoix("TempsSprint", 1)"  
    - func.py line 260: Montrer le temps à chaque pas
    - Pouvoir reprendre un exercice à un certain mot. 

    Lorsque Tilio fait le "choisir" il faut qu il lise le mot, l imagine puis trouve la correspondance. Une aide pourrait etre d afficher le mot sans les choix, appuyer sur une touche, afficher le choix, faire le choix. 

- Debug des fermetures soudaines de l'écrant de saisie lors d exercice par Tilio.
    Pour afficher le message d'erreur, apprendreList.py est encapsulé dans apprendre.bat ce qui donne la possibilité de voir un message d'erreur sans que la fenetre se ferme automatiquement. Les combinaisons clavier CTRL + T, CTRL + Z, CTRL + ENter (plusieur fois) provoquent des erreurs....

Découper la structure comme suite
0) Je choisis le temps du sprint
    Nombre de minutes pour un sprint (0 = je fais en un seul coup): 
1) Je me familiarise avec un nouveau voc
    - Je trouve un mots parmis plusieurs énemis/indiens (proposer un nombre d'énemis, trouver mot parmis N éléments)
    - Je pense au mot et je vérifie que c'est juste (réfléchir, voir réponse, décider juste ou faux)
2) J'exerce un vocabulaire
    - J'écris, je vois ma première erreur et le reste de la réponse juste
    - J'écris et je vois seulment ma première erreur
    - J'écris jusqu'à ce que ce soit juste (sans aide) 

Audio:
Ajouter du son. Employer Audigy pour découper des mots all enregistré par Ortrud,  lui demander un enregistrement du voc.
