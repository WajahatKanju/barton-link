Under heavy development.

# Barton Link
## Search and filter your revelations.

Barton Link is a tool for writers to organize excerpts of writing before (and after) they have been used in a writer's larger work.

Setup
```shell
cd barton-fink/ # cd into project root
pip install -e .[all] # See pyproject.toml for optional-dependencies
cd src/
python manage.py makemigrations
python manage.py migrate
```

Running Server
```shell
cd src/
python manage.py runserver
```
