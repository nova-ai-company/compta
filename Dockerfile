# --- Étape 1 : construction du site statique ---
FROM python:3.12-slim AS build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY outils/ outils/
COPY formation/ formation/
RUN python outils/gen_lexique.py && python outils/gen_mkdocs.py && mkdocs build

# --- Étape 2 : service par nginx (port fourni par Railway via $PORT) ---
FROM nginx:1.27-alpine
ENV PORT=8080
COPY outils/nginx.conf.template /etc/nginx/templates/default.conf.template
COPY --from=build /app/site /usr/share/nginx/html
