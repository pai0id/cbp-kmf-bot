FROM python:3.12-alpine

WORKDIR /bot

COPY requirements.txt .
COPY ./src/*.py .
COPY ./char_icons/*.png ./char_icons/

RUN pip install -r requirements.txt

EXPOSE 3012

CMD ["python3.12", "./bot.py"]
