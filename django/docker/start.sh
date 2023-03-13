#!/bin/bash
set -e
set -x

echo "Creating dirs and change folder permissions"
sudo mkdir -p $LOGS_ROOT $MEDIA_ROOT $STATIC_ROOT
sudo chown -R 1000:1000 $LOGS_ROOT $MEDIA_ROOT $STATIC_ROOT
sudo chmod -R 777 $LOGS_ROOT $MEDIA_ROOT $STATIC_ROOT
echo "Done!"

if [ "$MODE" = "development" ]; then
    echo "Creating migrations..."
    python3 manage.py makemigrations
    echo "Created!"
fi

echo "Migrating models..."
python manage.py migrate
echo "Migrated!"

echo "Loading fixtures..."
# python manage.py loaddata **/fixtures/default/*.json
# if [ "$MODE" = "development" ]; then
#     python manage.py loaddata **/fixtures/*.json
# fi
echo "Loaded!"


#echo "Compiling translations..."
#python manage.py compilemessages -v 0
#echo "Done!"

if [ "$MODE" = "production" ]; then
    echo "Coping default media..."
    sudo cp -a /code/biopark/media/. $MEDIA_ROOT
    echo "Done"

    echo "Changing media permissions"
    sudo chown -R 1000:1000 $MEDIA_ROOT
    sudo chmod -R 777 $MEDIA_ROOT
    echo "Done!"

    echo "Collecting statics..."
    python manage.py collectstatic --noinput -v 0
    echo "Collected"

    echo "Compressing..."
    python manage.py compress
    echo "Done"

    echo "Starting biopark as `whoami`" &
    exec gunicorn biopark.wsgi:application --name biopark \
        --timeout 300 \
        --workers $NUM_GUNICORN_WORKERS --bind 0.0.0.0:$DJANGO_PORT --log-level=info \
        --log-file=$LOGS_ROOT/gunicorn_log.log --access-logfile=$LOGS_ROOT/gunicorn_access.log

elif [ "$MODE" = "development" ]; then
    echo "Starting biopark as `whoami`"
    python manage.py runserver 0.0.0.0:8000
fi
