FROM python

WORKDIR /app

COPY . .

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y build-essential python3-pip

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "main.py"]



 