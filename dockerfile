#lelelel

FROM python:3-alpine

RUN apk update
RUN apk add git
RUN git clone https://github.com/um-computacion-tm/scrabble-2023-Juan-Martin-Valverde
WORKDIR /scrabble-2023-Juan-Martin-Valverde
RUN ls
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.main" ] 