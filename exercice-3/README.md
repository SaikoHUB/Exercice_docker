# Exercice 3 — Volumes et persistance des données

```bash
# 3.1 — Conteneur éphémère (le fichier disparait après exit)
docker run -it --rm alpine
# dans le conteneur :
mkdir /data && echo "bonjour" > /data/test.txt && exit
# Après relancement : fichier disparu car filesystem éphémère

# 3.2 — Bind mount
docker run -d -p 8080:80 \
  -v $(pwd)/html:/usr/share/nginx/html \
  nginx:alpine
# Modifier index.html sur la machine = changement immédiat dans le navigateur

# 3.3 — Créer un volume nommé
docker volume create mes-donnees

# 3.4 — Écrire dans le volume
docker run -it --rm -v mes-donnees:/data alpine
# dans le conteneur :
echo "je survis" > /data/persistant.txt && exit

# 3.5 — Vérifier la persistance dans un nouveau conteneur
docker run -it --rm -v mes-donnees:/data alpine cat /data/persistant.txt
# => "je survis" : le volume persiste indépendamment du cycle de vie du conteneur

# 3.6 — Lister les volumes
docker volume ls
# Stocké dans : /var/lib/docker/volumes/mes-donnees/_data

# 3.7 — Supprimer le volume
docker volume rm mes-donnees
# Précaution : s'assurer qu'aucun conteneur n'utilise le volume avant suppression
```
