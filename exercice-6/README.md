# Exercice 6 — Docker Compose : stack multi-services

```bash
# 6.5 — Démarrer la stack
docker compose up -d

# 6.6 — Tester le compteur et le reset
curl http://localhost:5000
curl http://localhost:5000/reset

# 6.7 — Redémarrer (le compteur persiste grâce au volume redis-data)
docker compose down
docker compose up -d

# 6.8 — Logs en temps réel
docker compose logs -f

# 6.9 — Shell dans le conteneur web
docker compose exec web sh

# 6.10 — Tout supprimer y compris volumes
docker compose down -v
```
