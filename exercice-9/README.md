# Exercice 9 — Stack complète : Flask + PostgreSQL + Nginx

```bash
# Lancer la stack
docker compose up -d

# Vérifier les healthchecks
docker compose ps

# Tester l'ajout de visites
curl -X POST http://localhost/visites
curl http://localhost/

# Vérifier la persistance après redémarrage
docker compose down
docker compose up -d
curl http://localhost/
```

## Points clés
- db n'expose aucun port sur l'hôte (sécurité)
- depends_on avec condition: service_healthy évite les erreurs de démarrage
- Deux réseaux : backend (db+app) et frontend (app+nginx)
