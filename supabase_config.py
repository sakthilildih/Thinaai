from decouple import config

# Supabase Database Configuration (sourced from environment variables)
# Set these in your deployment environment (e.g., Render Environment Variables)

DATABASE_CONFIG = {
    'NAME': config('DB_NAME', default='postgres'),
    'USER': config('DB_USER', default='postgres'),
    'PASSWORD': config('DB_PASSWORD', default=''),
    'HOST': config('DB_HOST', default='localhost'),
    'PORT': config('DB_PORT', default='5432'),
}

