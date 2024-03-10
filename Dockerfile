FROM python:3.12-alpine

WORKDIR /app

RUN python3 -m venv .venv && source .venv/bin/activate

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD sh -c "python3 manage.py runserver 0.0.0.0:8000"