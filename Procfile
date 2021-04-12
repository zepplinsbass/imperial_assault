web: gunicorn imperial-assault.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: celery worker --workdir backend --app=imperial-assault -B --loglevel=info
