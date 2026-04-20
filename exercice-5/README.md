# Exercice 5 — Containeriser un serveur Flask

```bash
# 5.4 — Construire l'image
docker build -t flask-app:v1 .

# 5.5 — Lancer avec variable d'environnement
docker run -d -p 5000:5000 -e APP_ENV=production flask-app:v1

# 5.6 — Relancer sans APP_ENV => affiche "développement" (valeur par défaut)
docker run -d -p 5000:5000 flask-app:v1

# 5.7 — Voir la taille
docker images flask-app:v1
# Pistes de réduction :
# 1) Multi-stage build
# 2) Image de base python:3.12-alpine (encore plus légère)
```

## Pourquoi l'ordre du Dockerfile est important ?
Copier requirements.txt AVANT le reste du code permet à Docker de mettre en cache
le layer "pip install". Si seul app.py change, pip n'est pas réexécuté.
