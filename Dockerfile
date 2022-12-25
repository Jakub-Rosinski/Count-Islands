FROM python:3.11

WORKDIR /count-islands
COPY . ./

ENTRYPOINT [ "python", "./main.py" ]