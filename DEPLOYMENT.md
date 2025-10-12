# DigitalOcean App Platform Deployment Guide

## Prerequisites

- GitHub repository with your code
- DigitalOcean account

## Deployment Steps

### 1. Push to GitHub

```bash
git add .
git commit -m "Prepare for DigitalOcean deployment"
git push origin main
```

### 2. Create DigitalOcean App

1. Go to [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)
2. Click "Create App"
3. Choose "GitHub" as source
4. Select your repository
5. Choose branch: `main`

### 3. Configure App Settings

- **Name**: Choose your app name (e.g., `thinaai`)
- **Region**: Choose closest to your users
- **Plan**: Start with Basic ($5/month)

### 4. Environment Variables

Set these in DigitalOcean App Platform dashboard:

```
SECRET_KEY=your-long-random-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.ondigitalocean.app,localhost,127.0.0.1
```

### 5. Build Settings

- **Build Command**: `python manage.py collectstatic --noinput`
- **Run Command**: `gunicorn studybud.wsgi:application`

### 6. Database

- **Current**: SQLite3 (file-based, included in deployment)
- **Future**: Can upgrade to PostgreSQL managed database

## Environment Variables Reference

| Variable        | Description       | Example                       |
| --------------- | ----------------- | ----------------------------- |
| `SECRET_KEY`    | Django secret key | `django-insecure-...`         |
| `DEBUG`         | Debug mode        | `False` for production        |
| `ALLOWED_HOSTS` | Allowed domains   | `your-app.ondigitalocean.app` |

## Post-Deployment

1. App will be available at: `https://your-app-name.ondigitalocean.app`
2. Admin panel: `https://your-app-name.ondigitalocean.app/admin/`
3. Create superuser: Use DigitalOcean console or local admin

## Troubleshooting

- Check logs in DigitalOcean dashboard
- Ensure all environment variables are set
- Verify `DEBUG=False` in production
- Check static files are collected properly

## Security Notes

- Never commit `.env` files
- Use strong `SECRET_KEY` in production
- Keep `DEBUG=False` in production
- HTTPS is automatically enabled by DigitalOcean
