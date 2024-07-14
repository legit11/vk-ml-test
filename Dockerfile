FROM python:3.12
WORKDIR /app
COPY . .
COPY requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 80
ENV NODE_ENV production
CMD ["python", "main.py"]
