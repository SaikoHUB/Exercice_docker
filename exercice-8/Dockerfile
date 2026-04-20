# Stage builder
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage final
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /install
ENV PYTHONPATH=/install/lib/python3.12/site-packages
COPY app.py .

# Utilisateur non-root
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
