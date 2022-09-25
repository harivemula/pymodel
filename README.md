# pymodel
Sample python model deployment using FastAPI to heroku.

# Steps to deploy in heroku
1. Install heroku cli (ubuntu) - `curl https://cli-assets.heroku.com/install-ubuntu.sh | sh`
2. Login - `heroku login`

```
mkdir pymodel
cd pymodel/
git init
heroku git:remote -a pymodel
git add .
git commit -am "initial iris sample"
git push heroku master

heroku logs --tail
```
