#!/bin/bash

if [[ "$1" == "celery" ]]; then
    celery --app=Fast_API_course.tasks.celery_task:celery worker --loglevel=info
elif [[ "$1" == "flower" ]]; then
    celery --app=Fast_API_course.tasks.celery_task:celery flower
fi
