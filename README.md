publipostage.py
===============

Envoyer par email un message personnalisé à quelques éléments de son carnet d'adresse.

Le problème
-----------

La situation est la suivante : un professeur désire envoyer par email, à chaque élève, un lien internet vers sa copie corrigée numériquement et déposée sur un cloud quelconque (google drive, dropbox etc.). Chaque lien étant différent, afin de préserver la confidentialité des échanges entre le professeur et l'élève, il faut envoyer un message différent à chaque élève.

Imaginons la classe fictive suivante, composée de deux élèves :

```
David Dupont (ddupont__at__gémèle__dot__com)
Emilie Durand (emdurand__at__hotte_mèle__dot_com)
```

Le message envoyé à chaque étudiant sera le suivant:

```bash
Bonjour David Dupont,

Vous pouvez télécharger votre copie en cliquant sur le lien suivant :
https://drive/lklkjglkjdljksd544334

Bien à vous,

Le professeur
```

et évidemment le deuxième qui aura la même forme, avec le nom qui change ainsi que le lien sur lequel cliquer.

Solution
--------
Un script Python qui automatise l'envoie de mail, à partir de la saisie des informations dans un tableau (MS Office, Excel etc.)

Etape 1
-------

Créer une nouvelle feuille, avec son tableau, qui contient trois colonnes : la première pour le nom de l'élève, la deuxième pour son adresse email, la troisième pour le lien à envoyer.

Etape 2
-------
Depuis le tableau, enregistrer la feuille dans un fichier au format CSV. Choisir le point virgule comme séparateur de champs.
Enregistrer ce fichier avec le nom ```coordonnees_eleves.csv```
Le fichier aura la forme suivante:

```bash
David Dupont; ddupont__at__gémèle__dot__com; https://fghlglfdhlkj654654654
Emilie Durand; emdurand__at__hotte_mèle__dot_com; https://fghlglfdhlkj654654997
[...]
```

Etape 3
-------
Il faut connaître l'adresse et le port du serveur SMTP qui va servir à l'envoi des messages. Si vous ne le connaissez pas, il suffit souvent de taper dans un moteur de recherche "SMTP orange.fr" ou "SMTP hotmail.fr", et on trouve l'information, qui est publque. Par exemple, pour le serveur qui gère les adresses académiques à ac-dijon.fr, c'est "hermes.ac-dijon.fr", port 465 (voir par exemple http://ien21-ouest.ac-dijon.fr/IMG/pdf/Configurer_Thunderbird_V5.pdf).

Une fois que vous avez cette information, éditer le script publipostage.py et changer les lignes en question. Vous devez aussi renseigner votre adresse email.

Etape 4
-------
Exécuter le script Python permettant d'envoyer un email à chaque élève.

```bash
$ python publipostage.py
```

Vous devez entrer le mot de passe qui vous permettra de vous connecter au serveur.

Remarque
--------
Une installation Python standard suffit, inutile de sortir l'artillerie lourde avec WinPython, anaconda etc.

Pour aller plus loin
--------------------
Le script Python est très simple, adaptable à toute situation similaire (avec plus de cases, personnalisation du message différente etc.)

Toute contribution pour améliorer la situation est la bienvenue.