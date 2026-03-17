FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]