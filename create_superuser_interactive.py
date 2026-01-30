#!/usr/bin/env python
"""
Interactive script to create Django superuser
Usage: python create_superuser_interactive.py
"""
import os
import sys
import django
import getpass

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser_interactive():
    """Create superuser interactively"""
    
    print("=" * 50)
    print("Django Superuser Creation")
    print("=" * 50)
    
    # Get username
    username = input("Username (default: admin): ").strip() or 'admin'
    
    # Check if username exists
    if User.objects.filter(username=username).exists():
        print(f'❌ Username "{username}" already exists!')
        return False
    
    # Get email
    email = input("Email (optional): ").strip() or ''
    
    # Get password
    while True:
        password = getpass.getpass("Password: ")
        password2 = getpass.getpass("Password (again): ")
        
        if password != password2:
            print("❌ Passwords don't match. Please try again.")
            continue
        
        if len(password) < 8:
            print("⚠️  Warning: Password is too short (minimum 8 characters)")
            confirm = input("Continue anyway? (y/n): ").strip().lower()
            if confirm != 'y':
                continue
        
        break
    
    # Create superuser
    try:
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f'\n✅ Superuser "{username}" created successfully!')
        return True
    except Exception as e:
        print(f'❌ Error creating superuser: {e}')
        return False

if __name__ == '__main__':
    create_superuser_interactive()
