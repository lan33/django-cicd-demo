# Utiliser une image Python légère
FROM python:3.13-slim

# Définir le répertoire de travail
WORKDIR /app

# Définir une variable d'environnement pour désactiver le buffering de sortie
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Copier le fichier requirements.txt pour installer les dépendances
COPY requirements.txt /app

# Installer les dépendances
RUN pip install -r requirements.txt --no-cache-dir

# Copier le contenu du projet dans le conteneur
COPY . /app

# Lancer les tests unitaires avec pytest
RUN pytest

# Exposer le port 8000
EXPOSE 8000

# Démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
