# Exercice 2 — Construire sa première image avec un Dockerfile

```bash
# 2.3 — Construire l'image
docker build -t mon-site:v1 .

# 2.4 — Lancer sur le port 9090 avec suppression auto
docker run --rm -p 9090:80 mon-site:v1

# 2.5 — Lister les images
docker images

# 2.6 — Inspecter les layers
docker history mon-site:v1
# 1 layer ajouté par rapport à nginx:alpine (le COPY)

# 2.7 — Reconstruire en v2 après modif de index.html
docker build -t mon-site:v2 .
# FROM nginx:alpine = cache / COPY = réexécuté car index.html a changé

# 2.8 — Supprimer v1 sans supprimer v2
docker rmi mon-site:v1
```
