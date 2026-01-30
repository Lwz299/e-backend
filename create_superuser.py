#!/usr/bin/env python
"""
Script to create Django superuser automatically
Usage: python create_superuser.py
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    """Create superuser if it doesn't exist"""
    
    # Default credentials (يمكنك تغييرها)
    username = os.environ.get('SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('SUPERUSER_EMAIL', 'admin@example.com')
    password = os.environ.get('SUPERUSER_PASSWORD', 'admin123456')
    
    # Check if superuser already exists
    if User.objects.filter(username=username).exists():
        print(f'⚠️  Superuser "{username}" already exists!')
        return False
    
    # Create superuser
    try:
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f'✅ Superuser "{username}" created successfully!')
        print(f'   Email: {email}')
        print(f'   Password: {password}')
        print('\n⚠️  Remember to change the password in production!')
        return True
    except Exception as e:
        print(f'❌ Error creating superuser: {e}')
        return False

if __name__ == '__main__':
    create_superuser()
