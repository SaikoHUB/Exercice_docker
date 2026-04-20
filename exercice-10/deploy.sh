#!/bin/bash

echo " Construction des images (--no-cache)..."
docker compose build --no-cache

echo " Lancement de la stack..."
docker compose up -d

echo " Attente que nginx soit disponible..."
for i in $(seq 1 60); do
  if curl -sf http://localhost/health > /dev/null 2>&1; then
    echo " Stack déployée avec succès"
    exit 0
  fi
  sleep 1
done

echo " Timeout — vérifiez les logs"
docker compose logs --tail=20
exit 1
