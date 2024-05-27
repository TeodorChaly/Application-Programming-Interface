FROM python:3.11

RUN mkdir /hotels

WORKDIR /hotels

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /hotels/docker/*.sh

CMD ["gunicorn", "Fast_API_course.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]