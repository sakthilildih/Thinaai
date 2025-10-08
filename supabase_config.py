<<<<<<< HEAD
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

=======
# Supabase Database Configuration
# Your actual Supabase credentials

DATABASE_CONFIG = {
    'NAME': 'postgres',
    'USER': 'postgres',
    'PASSWORD': 'Psycho.jocker2507',
    'HOST': 'db.gwmwmyxhhqhotefrsapf.supabase.co',
    'PORT': '5432',
}

# Example:
# DATABASE_CONFIG = {
#     'NAME': 'postgres',
#     'USER': 'postgres', 
#     'PASSWORD': 'mypassword123',
#     'HOST': 'abcdefghijklmnop.supabase.co',
#     'PORT': '5432',
# }
>>>>>>> e37136636f97fb49380ea0575e324f3448a5bf67
