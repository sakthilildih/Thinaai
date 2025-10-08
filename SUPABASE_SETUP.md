# Supabase Setup Guide

## Step 1: Get Your Supabase Credentials

1. Go to [supabase.com](https://supabase.com) and sign in
2. Create a new project or use an existing one
3. Go to **Settings** → **Database**
4. Copy the following information:
   - **Database Name**: Usually `postgres`
   - **Username**: Usually `postgres`
   - **Password**: Your database password
   - **Host**: Your project URL (e.g., `abcdefghijklmnop.supabase.co`)
   - **Port**: `5432`

## Step 2: Configure Your Database Connection

### Option A: Using Environment Variables (Recommended)

Create a `.env` file in your project root:

```env
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your_supabase_password_here
DB_HOST=your_project_ref.supabase.co
DB_PORT=5432
```

### Option B: Using supabase_config.py

Edit the `supabase_config.py` file and replace the placeholder values:

```python
DATABASE_CONFIG = {
    'NAME': 'postgres',
    'USER': 'postgres',
    'PASSWORD': 'your_actual_password',
    'HOST': 'your_project_ref.supabase.co',
    'PORT': '5432',
}
```

Then uncomment the configuration in `settings.py` and comment out the environment variable version.

## Step 3: Run Migrations

After configuring your database credentials, run:

```bash
python manage.py migrate
```

## Step 4: Create Superuser

```bash
python manage.py createsuperuser
```

## Step 5: Test Your Application

```bash
python manage.py runserver
```

Your Django application is now connected to Supabase PostgreSQL! 🎉
