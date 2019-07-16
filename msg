source venv/bin/activate
python manage.py makemessages -i venv
cd jauth
python ../manage.py compilemessages
