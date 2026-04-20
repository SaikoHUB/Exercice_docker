# Exercice 4 — Réseaux Docker

```bash
# 4.1 — Lister les réseaux (3 par défaut : bridge, host, none)
docker network ls

# 4.2 — Créer un réseau bridge personnalisé
docker network create mon-reseau

# 4.3 — Lancer serveur-web sur mon-reseau
docker run -d --name serveur-web --network mon-reseau nginx:alpine

# 4.4 — Lancer client et tester la résolution DNS
docker run -it --name client --network mon-reseau alpine
# dans le conteneur :
wget -qO- http://serveur-web
# => page HTML de nginx
# Raison : DNS automatique sur les réseaux bridge personnalisés

# 4.5 — Client sans le réseau personnalisé (résolution DNS échoue)
docker run -it --name client-externe alpine
# wget http://serveur-web => échec : pas de DNS sur bridge par défaut

# 4.6 — Connecter client-externe après démarrage
docker network connect mon-reseau client-externe

# 4.7 — Nettoyage
docker stop serveur-web client client-externe
docker rm serveur-web client client-externe
docker network rm mon-reseau
```
