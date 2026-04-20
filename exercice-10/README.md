# Exercice 10 — Sécurité, optimisation avancée et debugging

## Partie A — Audit

```bash
# 10.1 — Inspecter l'image
docker image inspect exercice-10-app
# Risques visibles : utilisateur root, variables d'env avec secrets

# 10.2 — Contraintes de sécurité (voir compose.yaml)
# no-new-privileges : empêche l'élévation de privilèges via setuid
# read_only : filesystem en lecture seule
# tmpfs /tmp : espace temporaire en mémoire

# 10.3 — Limites ressources (voir compose.yaml)
# limits = valeur maximale / reservations = garanti même sous charge
```

## Partie B — Debugging

```bash
# 10.4 — Simuler une panne DB
docker compose stop db
docker compose ps
# => app passe en unhealthy

# 10.5 — 20 dernières lignes de logs du service app
docker compose logs --tail=20 app

# 10.6 — Monitorer les ressources
docker stats

# 10.7 — Variables d'env sans ouvrir de shell
docker inspect exercice-10-app-1 --format '{{json .Config.Env}}'
# Risque : les secrets sont lisibles en clair par tout admin Docker
```

## Partie C — Bonnes pratiques

```bash
# 10.8 — HEALTHCHECK Dockerfile vs compose.yaml
# Dockerfile = embarqué dans l'image, utilisé partout
# compose.yaml = spécifique au déploiement, a la PRIORITÉ

# 10.9 — Ordre optimal pour le cache Docker
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY . .
# => pip install mis en cache si seul app.py change

# 10.10 — Script de déploiement
chmod +x deploy.sh && ./deploy.sh
```
