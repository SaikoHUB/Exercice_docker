# Exercice 8 — Optimisation : multi-stage build, .dockerignore et non-root

```bash
# 8.1 — Construire la version naïve
docker build -f Dockerfile.naive -t app-naive:v1 .

# 8.3/8.4 — Construire la version optimisée et comparer
docker build -t app-optimisee:v1 .
docker images

# 8.5/8.6 — Vérifier que le process tourne en non-root
docker run --rm app-optimisee:v1 whoami
# => appuser

# 8.7 — Lister les images triées par taille
docker images --format '{{.Repository}}:{{.Tag}}\t{{.Size}}' | sort -k2 -h -r
```

## Pourquoi exclure tests/ du contexte de build ?
Les tests ne sont pas nécessaires en prod. Exclure via .dockerignore réduit le contexte
envoyé au daemon et évite d'inclure du code inutile dans l'image finale.

## Pourquoi éviter root dans un conteneur ?
Si un attaquant exploite une faille, il obtient les privilèges root dans le conteneur,
ce qui peut permettre de s'échapper vers l'hôte.
