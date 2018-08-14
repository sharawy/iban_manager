FROM python:3.5
ENV PYTHONUNBUFFERED 1

# Update the default application repository sources list
RUN apt-get -qq update && \
    apt-get install -y \
    python-dev \
    python \
    python-pip \
    python-setuptools \
    build-essential \
    postgresql-server-dev-all \
    libjpeg-dev \
    binutils \
    libproj-dev \
    libgeos-dev \
    gdal-bin \
    git \
    gettext \
    python-lxml \
    python-cffi \
    libcairo2 \
    libpango1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    curl \
    sudo




ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt


ADD . /app
WORKDIR /app

RUN python manage.py collectstatic --no-input




EXPOSE 8000
ENV PORT 8000

CMD ["uwsgi","--ini", "/app/iban_manager/wsgi/uwsgi.ini"]

