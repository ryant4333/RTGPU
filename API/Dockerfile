FROM python:3.12-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app/ /code/

EXPOSE 8000

CMD ["fastapi", "run", "dummy_app.py", "--port", "8000"]