FROM python:3.11
WORKDIR /bot
COPY . /bot
RUN pip install -r requirements.txt
CMD python main.py