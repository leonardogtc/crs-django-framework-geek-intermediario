## Comandos:
python3 -m venv venv
source venv/bin/activate
pip install pip setuptools wheel --upgrade
pip install django
pip install gunicorn
pip install whitenoise
pip freeze > requirements.txt