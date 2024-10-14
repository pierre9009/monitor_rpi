# Utiliser l'image de base Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier de requirements si nécessaire
COPY requirements.txt requirements.txt

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port 5000
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "app.py"]
