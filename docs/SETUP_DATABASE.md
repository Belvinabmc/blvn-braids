# SETUP-04 — Configuration de la base de données MySQL

## Objectif

Configurer MySQL pour le projet **Blvn_Braids** et connecter le backend Django à la base de données MySQL.

Architecture obtenue :

```text
Frontend React
      ↓
Backend Django
      ↓
mysqlclient
      ↓
MySQL
      ↓
Base blvn_braids
```

---

# 1. Vérifier MySQL

Commande utilisée :

```powershell
mysql --version
```

La commande `mysql` n'était pas directement disponible dans le PATH Windows.

Nous avons donc vérifié les services MySQL présents :

```powershell
Get-Service *mysql* -ErrorAction SilentlyContinue
```

Résultat :

```text
wampmysqld64
```

MySQL est installé avec **WampServer**.

---

# 2. Démarrer MySQL

Le service MySQL était initialement arrêté.

Après démarrage depuis WampServer, la vérification :

```powershell
Get-Service *mysql* -ErrorAction SilentlyContinue
```

a indiqué :

```text
Running  wampmysqld64
```

Le serveur MySQL fonctionne donc correctement.

---

# 3. Créer la base de données

La base de données du projet a été créée avec le nom :

```text
blvn_braids
```

Cette base contiendra plus tard les données de l'application :

- utilisateurs ;
- prestations ;
- réservations ;
- créneaux ;
- paiements ;
- horaires ;
- fermetures ;
- galerie.

---

# 4. Créer un utilisateur MySQL dédié

Un utilisateur MySQL spécifique au projet a été créé :

```text
blvn_braids_user
```

Commande utilisée :

```sql
CREATE USER 'blvn_braids_user'@'localhost'
IDENTIFIED BY 'MOT_DE_PASSE_PRIVE';
```

Le véritable mot de passe n'est volontairement pas écrit dans cette documentation.

---

# 5. Donner les droits sur la base

Commande utilisée :

```sql
GRANT ALL PRIVILEGES ON blvn_braids.*
TO 'blvn_braids_user'@'localhost';
```

L'utilisateur `blvn_braids_user` peut donc travailler sur la base :

```text
blvn_braids
```

sans utiliser directement le compte administrateur MySQL `root`.

---

# 6. Installer le connecteur MySQL pour Django

Activation de l'environnement virtuel Python :

```powershell
.\.venv\Scripts\Activate.ps1
```

Installation du connecteur :

```bash
pip install mysqlclient
```

`mysqlclient` permet à Django de communiquer avec MySQL.

```text
Django
   ↓
mysqlclient
   ↓
MySQL
```

---

# 7. Installer python-dotenv

Commande :

```bash
pip install python-dotenv
```

`python-dotenv` permet à Django de charger les variables sensibles depuis un fichier `.env`.

---

# 8. Créer le fichier .env

Le fichier suivant a été créé à la racine du projet :

```text
blvn-braids/.env
```

Structure utilisée :

```env
DJANGO_SECRET_KEY=CLE_SECRETE_PRIVEE
DJANGO_DEBUG=True

DB_NAME=blvn_braids
DB_USER=blvn_braids_user
DB_PASSWORD=MOT_DE_PASSE_PRIVE
DB_HOST=localhost
DB_PORT=3306
```

Les vraies valeurs sensibles ne doivent jamais être ajoutées à cette documentation.

Le fichier `.env` est ignoré par Git grâce à `.gitignore`.

---

# 9. Générer une clé secrète Django

Commande utilisée :

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

La clé générée est enregistrée uniquement dans :

```text
.env
```

Elle ne doit pas être envoyée sur GitHub.

---

# 10. Charger le fichier .env dans Django

Dans :

```text
backend/config/settings.py
```

les imports suivants sont utilisés :

```python
from pathlib import Path
import os

from dotenv import load_dotenv
```

Puis :

```python
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = BASE_DIR.parent

load_dotenv(ROOT_DIR / ".env")
```

Django peut ainsi lire les variables stockées dans `.env`.

---

# 11. Configurer Django pour MySQL

La configuration de la base de données dans `settings.py` est :

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "3306"),
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

---

# 12. Encodage utf8mb4

Cette option :

```python
"charset": "utf8mb4"
```

permet à MySQL de stocker correctement :

- les accents ;
- les caractères spéciaux ;
- les emojis ;
- les caractères Unicode.

---

# 13. MySQL Strict Mode

Cette option :

```python
"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
```

active le mode strict MySQL.

Cela permet d'éviter que certaines données invalides soient silencieusement modifiées ou tronquées par MySQL.

---

# 14. Tester la connexion Django → MySQL

Depuis :

```text
backend/
```

commande utilisée :

```bash
python manage.py migrate
```

Les migrations Django ont été appliquées avec succès :

```text
Applying ... OK
```

Cela confirme que Django arrive à communiquer avec la base MySQL `blvn_braids`.

---

# 15. Vérifier les migrations

Après activation du mode strict, la commande :

```bash
python manage.py migrate
```

a retourné :

```text
No migrations to apply.
```

Cela signifie :

- la connexion MySQL fonctionne ;
- les migrations sont déjà appliquées ;
- la configuration est valide.

---

# 16. Mettre à jour requirements.txt

Les nouvelles dépendances Python doivent être enregistrées.

Depuis le dossier `backend` :

```bash
pip freeze > requirements.txt
```

Le fichier contient notamment :

```text
Django
mysqlclient
python-dotenv
```

ainsi que leurs dépendances.

---

# Sécurité

Les informations suivantes ne doivent jamais être envoyées sur GitHub :

```text
.env
.venv/
db.sqlite3
```

Les mots de passe et clés secrètes ne doivent jamais être écrits directement dans :

```text
settings.py
```

Les valeurs sensibles sont stockées dans :

```text
.env
```

---

# Architecture finale de la connexion

```text
backend/config/settings.py
          ↓
        .env
          ↓
       Django
          ↓
     mysqlclient
          ↓
       MySQL
          ↓
   blvn_braids
```

---
