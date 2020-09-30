FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN mkdir app
WORKDIR /app

COPY ./ /app/

RUN /usr/local/bin/python   -m pip install --upgrade pip
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --no-cache-dir -r requirements.txt \

ENV TZ Asia/Almaty
