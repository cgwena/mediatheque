#Instructions concernant l'exécution du programme
##Afin de pouvoir utiliser ce logiciel, vous devez exécuter les étapes suivantes :
Installation de Python sur votre ordinateur.
Le logiciel a été créé avec Python3, il faut donc installer cette version de Python. 
Vous pouvez télécharger Python à partir du site officiel : https://www.python.org/downloads/
##Téléchargement du logiciel :
Le logiciel se trouve sur ce site : https://github.com/cgwena/mediatheque
Pour le récupérer, vous devez cliquer sur Download zip :
Il faut ensuite ouvrir le dossier avec un IDE (PyCharm, VSCode...)
##Afin d'isoler les dépendances du projet, vous devez créer un environnement virtuel : dans le terminal de votre IDE, tapez la ligne de commande :
  python3 -m venv env
puis pour activer l'environnement virtuel : 
  source env/bin/activate 
##Allez ensuite dans le dossier « mediatheque » : 
	cd mediatheque
	Puis lancez le serveur de développement : 
	python3 manage.py runserver
