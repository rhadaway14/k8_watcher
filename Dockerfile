FROM python:3.9
WORKDIR /app
COPY main.py .
RUN apt-get update && apt-get install -y apt-transport-https gnupg2 curl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN chmod +x kubectl && mv kubectl /usr/local/bin/
RUN pip install kubernetes
CMD ["python", "main.py"]