FROM frolvlad/alpine-python3
MAINTAINER andrecogno@hotmail.it

RUN apk add --no-cache build-base jpeg-dev zlib-dev
RUN apk add --no-cache python3-dev
RUN apk add --no-cache freetype-dev

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD main.py main.py

ADD go_template.jpg go_template.jpg
ADD Go-Mono.ttf Go-Mono.ttf
ADD templates/ templates/

CMD python3 main.py
EXPOSE 5000
