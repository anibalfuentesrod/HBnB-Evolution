FROM python:3.8-alpine

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=5000

# setting the working directory
WORKDIR /app

# copy any requirements and install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# copies the app source code into container
COPY . /app/

# defining volume for persistent storage of data
VOLUME /app/data

# port that the app will run on
EXPOSE $PORT

# starting the Flask app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:${PORT}", "-v", "app:app"]

