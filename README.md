# TP noté Architecture logiciel 

## Lancement de l'applciation : 

Pour lancer l'application, il y a deux étapes :

- Il faut dans un premier temps mettre en route le server REST : 

```bash
cd quiz/
flask init_database
flask run
```

- On se met après dans un autre terminal pour lancer le client : 

```bash
npm install
npm run dev --host
```

## Choix de modélisation 

Pour réaliser se TP, nous avons choisi de faire 4 components différents : 

- Questionnaires : Représente la liste des questionnaires, lorsque l'utilisateur clique sur le bouton pour afficher les questionnaires, on fetch le serveur pour récupérer tous les questionnaires.
- Questionnaire : Permet l'affichage d'un questionnaire, appelé par un v-for dans Questionnaires, ce component gère les évenement sur les questionnaires, et les renvoie au parent qui les traitent.
- Questions : On a ici le même principe avec les questions, ce component représente la liste des questions d'un questionnaire. 
- Question : Affiche le détail d'une question et gère les évenements sur les questions, renvoyées au parent qui les traitent. 

## Réalisé par 

Sottier Liam

Mechain Romain