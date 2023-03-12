FROM python:3.11.2-bullseye

WORKDIR .

ENV PYTHONPATH=.

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "-u", "app/main.py"]