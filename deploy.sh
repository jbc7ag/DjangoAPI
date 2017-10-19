#!/usr/bin/env bash
echo "Mandando a Heroku"
sudo heroku container:login
sudo heroku container:push web --app $HEROKU_APP_NAME
echo "Se mando a Heroku"