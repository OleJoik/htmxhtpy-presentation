# HTMX-HTPY Presentation

## Requirements

- Tailwind CLI


## Develop

`uvicorn src.htmxhtpy.main:app --host 0.0.0.0 --port 8080 --reload`

# Styling

`tailwindcss -i src/htmxhtpy/tailwind.css -o static/styles.css --watch`

## Deploy

`git push heroku main`

Seeing logs in heroku:

`heroku logs --tail`
