from decouple import config

# Supabase Database Configuration (via environment variables)
# Set these in Render/locally as env vars

DATABASE_CONFIG = {
    'NAME': config('DB_NAME', default='postgres'),
    'USER': config('DB_USER', default='postgres'),
    'PASSWORD': config('DB_PASSWORD', default=''),
    'HOST': config('DB_HOST', default='localhost'),
    'PORT': config('DB_PORT', default='5432'),
}

