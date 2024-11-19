
#FROM python:slim


# Install PostgreSQL development tools
#RUN apt-get update && apt-get install -y \
 #   libpq-dev gcc \
 #   && rm -rf /var/lib/apt/lists/*


# Install Python dependencies
#COPY requirements.txt requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install gunicorn pymysql cryptography

# Copy application files
#COPY app app
#COPY migrations migrations
#COPY microblog.py config.py boot.sh ./
#RUN chmod a+x boot.sh

#ENV FLASK_APP microblog.py
#RUN flask translate compile

#EXPOSE 5000
#ENTRYPOINT ["./boot.sh"]

FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

#CMD ["python", "microblog.py"]
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

