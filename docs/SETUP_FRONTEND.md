# SETUP-03 — Initialisation du frontend React

## Objectif

Initialiser le frontend React du projet **BLVN_Braids** avec Vite et vérifier qu'il fonctionne correctement en local.

Le frontend aura notamment pour rôle de :

- afficher la page d'accueil ;
- afficher les prestations ;
- afficher le détail d'une prestation ;
- afficher la galerie ;
- permettre l'inscription et la connexion ;
- afficher les créneaux disponibles ;
- permettre la réservation ;
- afficher le résumé d'une réservation ;
- permettre la consultation et l'annulation des réservations ;
- afficher l'espace administratrice ;
- communiquer avec le backend Django via une API.

---

# 1. Vérifier Node.js

Commande utilisée :

```bash
node --version
```

Résultat obtenu :

```text
v24.16.0
```

Node.js est donc correctement installé sur la machine.

---

# 2. Vérifier npm

Commande utilisée :

```bash
npm --version
```

Résultat obtenu :

```text
11.13.0
```

`npm` est le gestionnaire de paquets utilisé avec Node.js.

Il permettra notamment :

- d'installer les dépendances du frontend ;
- de lancer le serveur de développement ;
- d'ajouter de futures bibliothèques React.

---

# 3. Désactiver l'environnement virtuel Python

L'environnement `.venv` utilisé pour Django était encore actif.

Commande utilisée :

```bash
deactivate
```

Cela permet de revenir à un terminal normal avant de travailler sur le frontend.

---

# 4. Créer le frontend React avec Vite

Depuis la racine du projet BLVN_Braids :

```bash
npm create vite@latest frontend -- --template react
```

Cette commande permet de :

- créer un dossier `frontend/` ;
- utiliser Vite comme outil de développement ;
- utiliser React comme bibliothèque frontend.

---

# 5. Structure générée

Après la création du frontend, la structure ressemble notamment à :

```text
frontend/
├── public/
├── src/
├── .gitignore
├── eslint.config.js
├── index.html
├── package.json
├── package-lock.json
└── vite.config.js
```

Le dossier `src/` contient le code principal de l'application React.

---

# 6. Installer les dépendances

Se placer dans le dossier frontend :

```bash
cd frontend
```

Puis installer les dépendances si nécessaire :

```bash
npm install
```

Cette commande lit le fichier :

```text
package.json
```

et installe les dépendances nécessaires dans :

```text
node_modules/
```

---

# 7. Démarrer le serveur React

Depuis le dossier `frontend` :

```bash
npm run dev
```

Vite démarre alors un serveur de développement local.

Adresse obtenue :

```text
http://localhost:5173/
```

---

# 8. Vérifier le fonctionnement dans le navigateur

Ouvrir :

```text
http://localhost:5173/
```

La page par défaut React / Vite doit apparaître.

Si la page s'affiche correctement, cela signifie que le frontend fonctionne.

---

# 9. Arrêter le serveur

Dans le terminal :

```text
Ctrl + C
```

Cela arrête le serveur de développement Vite.

---

# 10. Fichiers importants du frontend

## package.json

Contient notamment :

- le nom du projet ;
- les dépendances ;
- les scripts npm ;
- la configuration générale du projet Node.js.

---

## package-lock.json

Enregistre les versions exactes des dépendances installées.

Il doit être conservé dans Git.

---

## src/

Contient le code source principal de l'application React.

C'est ici que seront créés plus tard :

- les composants ;
- les pages ;
- les formulaires ;
- les interfaces ;
- la logique côté frontend.

---

## public/

Contient les fichiers publics statiques.

Exemples :

- images ;
- icônes ;
- favicon.

---

## vite.config.js

Contient la configuration de Vite.

Nous pourrons notamment l'utiliser plus tard pour certaines configurations du projet.

---

# 11. Vérifier que node_modules n'est pas envoyé sur GitHub

Le dossier :

```text
node_modules/
```

contient toutes les dépendances installées localement.

Il ne doit pas être envoyé sur GitHub.

Le `.gitignore` du projet contient déjà :

```gitignore
node_modules/
```

---

# 12. Nettoyer le projet React par défaut

Avant de commencer le véritable design BLVN_Braids, les éléments de démonstration créés automatiquement par Vite devront être supprimés ou remplacés.

Les principaux fichiers concernés sont notamment dans :

```text
frontend/src/
```

Le nettoyage sera effectué avant la création des vraies pages du projet.

---

# 13. Vérifier Git

Depuis la racine de BLVN_Braids :

```bash
git status
```

Cette commande permet de vérifier les fichiers nouveaux ou modifiés avant le commit.

---

# 14. Ajouter le frontend à Git

Depuis la racine du projet :

```bash
git add frontend docs/SETUP_FRONTEND.md
```

---

# 15. Créer le commit

Exemple de message :

```bash
git commit -m "setup: initialize React frontend"
```

---

# 16. Envoyer le frontend sur GitHub

Commande :

```bash
git push
```

---

# Structure générale après SETUP-03

La structure du projet devrait ressembler à :

```text
blvn-braids/
├── backend/
│   ├── config/
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── docs/
│   ├── SETUP_BACKEND.md
│   └── SETUP_FRONTEND.md
│
├── .gitignore
└── README.md
```

---



