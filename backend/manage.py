from django.core.management import execute_from_command_line
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

if __name__ == '__main__':
    execute_from_command_line()
