# Thomas Paviot, 2020 tpaviot@gmail.com
# Vous pouvez utiliser ce script comme bon vous semble.

import email
import smtplib
import os
from getpass import getpass

# création de la connexion au serveur
# changer la ligne suivante pour qu'elle corresponde au nom et au port
# du serveur SMTP qui va envoyer l'email.

s = smtplib.SMTP("machin.ac-lamaison.fr", 145)
s.ehlo()
s.starttls()  # utilisation de TLS
s.ehlo()

addr_expediteur = "leprofesseur@confinement.fr"  # cette adresse ne change pas

# connexion
# la ligne suivante permet de taper le mot de passe sans qu'il apparaisse en clair à l'écran
password = getpass("Veuillez entrer votre mot de passe :")
s.login(addr_expediteur, password)

# on ouvre le fichier en mode lecture
csv_file = os.path.join(".", "coordonnees_eleves.csv")
contenu_fichier = open(csv_file, "r")

# le modèle d'email qui va être envoyé à chaque destinataire. %s est une chaîne de caractère
# qui sera différente dans chaque email. Pour pouvoir faire les choses proprement, on pourrait utiliser
# un "moteur de template", style jinja, mais pour l'instant ça suffit.

# attention, dans ce modèle il faut au moins un saut de ligne en début de corps de message,
# sinon ça ne fonctionne pas.

MODELE_EMAIL = """

Bonjour %s,

Veuillez trouver votre copie en suivant le lien suivant :
%s

Bien à vous,

Le professeur

"""

# Ensuite on boucle sur les lignes du fichier csv pour construire chaque email
# et l'envoyer
for ligne in contenu_fichier:
    # on récupère le nom de l'élève
    nom_eleve, mail_destinataire, lien_vers_le_fichier = ligne.split(";")
    # on crée le contenu du message à partir du modèle
    contenu_message = MODELE_EMAIL % (nom_eleve, lien_vers_le_fichier)
    # ensuite on crée le message
    msg = email.message_from_string(contenu_message)  # le contenu
    msg['From'] = expediteur  #  email de l'expéditeur
    msg['To'] = mail_destinataire  # email du destinataire
    msg['Subject'] = contenu_message  # le corps du message du mail
    # si on veut on peut décommenter la ligne suivante pour voir ce qui va être envoyé
    # print(msg)
    # envoi du message
    s.sendmail(expediteur, mail_destinataire, msg.as_string())

# finalement on ferme le fichier
contenu_fichier.close()
# ainsi que la connexion
s.quit()
