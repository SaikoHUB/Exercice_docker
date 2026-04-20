# Exercice 7 — Variables d'environnement, .env et surcharge

```bash
# 7.5 — Lancer la stack
docker compose up -d

# 7.6 — Afficher le Compose après interpolation des variables
docker compose config

# 7.7 — Surcharger APP_PORT sans modifier .env
APP_PORT=9090 docker compose up -d

# 7.8 — Priorité des variables (du plus fort au plus faible) :
# 1) Variable dans le shell
# 2) Variable dans .env
# 3) Valeur par défaut dans compose.yaml
```

## 7.9 — Méthodes sécurisées pour les secrets en production
1. Docker Secrets (Swarm) — monte les secrets dans /run/secrets/
2. Gestionnaire externe : HashiCorp Vault, AWS Secrets Manager, Azure Key Vault
