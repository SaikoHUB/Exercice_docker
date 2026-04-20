# Exercice 1 — Premier contact avec Docker

## Commandes

```bash
# 1.1 — Télécharger l'image sans lancer de conteneur
docker pull nginx:alpine

# 1.2 — Lancer le conteneur en arrière-plan
docker run -d --name mon-nginx -p 8080:80 nginx:alpine

# 1.3 — Lister les conteneurs en cours d'exécution
docker ps

# 1.4 — Afficher les logs
docker logs mon-nginx

# 1.5 — Arrêter sans supprimer, puis lister TOUS les conteneurs
docker stop mon-nginx
docker ps -a
# Différence : docker ps = actifs seulement / docker ps -a = tous (y compris stoppés)

# 1.6 — Supprimer le conteneur
docker rm mon-nginx

# 1.7 — Commande pour suppression automatique à l'arrêt
docker run -d --rm --name mon-nginx -p 8080:80 nginx:alpine
```
