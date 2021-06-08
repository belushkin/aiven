FROM python:3

ENV APP_HOME=/usr/src/app

# create the app user
RUN groupadd --gid 1000 app \
  && useradd --uid 1000 --gid app --shell /bin/bash --create-home app \
  && mkdir $APP_HOME

# set work directory
WORKDIR $APP_HOME

# Install Python dependencies
RUN pip install --upgrade pip==21.0.1
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY . $APP_HOME

RUN chown -R app:app $APP_HOME
USER app

CMD [ "python", "./src/app.py" ]
