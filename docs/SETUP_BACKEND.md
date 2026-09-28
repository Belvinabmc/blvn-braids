# SETUP-02 — Initialisation du backend Django

## Objectif

Initialiser le backend Django du projet **BLVN_Braids** et préparer un environnement de développement propre.

Le backend aura notamment pour rôle de :

- gérer les utilisateurs ;
- gérer les prestations ;
- gérer les réservations ;
- gérer les créneaux ;
- gérer les paiements ;
- communiquer avec la base de données ;
- communiquer avec Stripe ;
- envoyer les informations nécessaires au frontend.

---

# 1. Vérifier Python

Commande utilisée :

```bash
python --version
```

Résultat obtenu :

```text
Python 3.12.6
```

Python est donc correctement installé sur la machine.

---

# 2. Vérifier pip

Commande utilisée :

```bash
pip --version
```

Résultat obtenu :

```text
pip 25.2
```

`pip` est le gestionnaire de paquets Python.

Il permettra notamment d'installer Django et les autres dépendances Python utilisées dans le projet.

---

# 3. Créer l'environnement virtuel

Depuis la racine du projet :

```bash
python -m venv .venv
```

Cette commande crée le dossier :

```text
.venv/
```

L'environnement virtuel permet d'isoler les dépendances Python de BLVN_Braids des autres projets présents sur l'ordinateur.

---

# 4. Activer l'environnement virtuel

Sous Windows avec PowerShell :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Puis :

```powershell
.\.venv\Scripts\Activate.ps1
```

Lorsque l'environnement virtuel est actif, le terminal doit normalement afficher quelque chose comme :

```text
(.venv)
```

devant le chemin du projet.

Exemple :

```text
(.venv) PS C:\Users\Valencia\Desktop\blvn-braids>
```

---

# 5. Vérifier que `.venv` n'est pas envoyé sur GitHub

Le dossier `.venv` contient les dépendances installées localement.

Il ne doit pas être envoyé sur GitHub.

Le fichier `.gitignore` doit donc contenir :

```gitignore
.venv/
```

---

# 6. Installer Django

Lorsque l'environnement virtuel est activé :

```bash
pip install django
```

Cette commande installe Django uniquement dans l'environnement virtuel du projet.

---

# 7. Vérifier l'installation de Django

Commande :

```bash
django-admin --version
```

Cette commande permet de vérifier que Django est correctement installé.

---

# 8. Créer le dossier backend

À la racine du projet BLVN_Braids, créer le dossier :

```text
backend/
```

La structure commencera alors à ressembler à :

```text
blvn-braids/
├── backend/
├── docs/
├── .venv/
├── .gitignore
└── README.md
```

---

# 9. Initialiser le projet Django

Se déplacer dans le dossier backend :

```bash
cd backend
```

Puis créer le projet Django :

```bash
django-admin startproject config .
```

Le `.` à la fin signifie que Django doit créer le projet directement dans le dossier `backend`.

La structure obtenue sera approximativement :

```text
backend/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---

# 10. Comprendre les fichiers principaux

## manage.py

Fichier permettant d'exécuter les commandes Django.

Exemples :

```bash
python manage.py runserver
```

```bash
python manage.py migrate
```

---

## config/settings.py

Contient la configuration générale du backend Django.

On y configurera plus tard notamment :

- les applications Django ;
- la base de données ;
- les variables de configuration ;
- la sécurité ;
- les paramètres liés à l'API.

---

## config/urls.py

Contient les routes principales du projet Django.

Les futures URL de l'API seront reliées depuis ce fichier.

---

## config/wsgi.py

Utilisé notamment pour déployer l'application Django sur un serveur compatible WSGI.

---

## config/asgi.py

Permet notamment à Django de fonctionner avec ASGI et des fonctionnalités asynchrones.

---

# 11. Lancer les migrations initiales

Depuis le dossier `backend` :

```bash
python manage.py migrate
```

Les migrations permettent à Django de créer les tables nécessaires à son fonctionnement.

À ce stade, Django utilisera sa configuration de base avant que nous configurions notre base de données définitive.

---

# 12. Démarrer le serveur Django

Commande :

```bash
python manage.py runserver
```

Django doit afficher une adresse locale similaire à :

```text
http://127.0.0.1:8000/
```

Ouvrir cette adresse dans le navigateur.

Si la page Django apparaît, cela signifie que le backend fonctionne correctement.

---

# 13. Arrêter le serveur Django

Dans le terminal :

```text
Ctrl + C
```

Cela arrête le serveur de développement.

---

# 14. Vérifier l'état Git

Depuis la racine du projet :

```bash
git status
```

Cette commande permet de voir :

- les nouveaux fichiers ;
- les fichiers modifiés ;
- les fichiers ignorés ou non suivis.

---

# 15. Vérifier que `.venv` n'apparaît pas dans Git

Le dossier :

```text
.venv/
```

ne doit pas être ajouté au dépôt Git.

Il doit être ignoré grâce au fichier :

```text
.gitignore
```

---

# 16. Enregistrer les dépendances Python

Une fois Django installé :

```bash
pip freeze > requirements.txt
```

Cette commande crée un fichier :

```text
requirements.txt
```

Il contient les dépendances Python utilisées par le backend.

Cela permettra plus tard de réinstaller les mêmes dépendances avec :

```bash
pip install -r requirements.txt
```

---

# 17. Ajouter les fichiers à Git

Après vérification :

```bash
git add .
```

---

# 18. Créer le commit

Exemple :

```bash
git commit -m "setup: initialize Django backend"
```

---

# 19. Envoyer les modifications sur GitHub

Commande :

```bash
git push
```

---

# Structure attendue après SETUP-02

La structure générale devrait ressembler à :

```text
blvn-braids/
├── backend/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   └── manage.py
│
├── docs/
│   └── SETUP_BACKEND.md
│
├── .venv/
├── .gitignore
├── README.md
└── requirements.txt
```

---


