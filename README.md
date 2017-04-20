# Build Chatbot with Facebook API, Heroku and Python

## Modified from https://github.com/lemonlatte/myCurrencyBot

## 1. Install Heroku (Follow the instructions)
https://devcenter.heroku.com/start

## 2. Clone this Repository 

## 3. Get Facebook API
Create a Page in the facebook 

Go to facebook developer to get your **PAGE_TOKEN**, which is unique and have to keep it as a secret.

**Copy** your **PAGE_TOKEN** into app.py

Set **BOT_TOKEN** as any string you want, you will use it later.

## 4. In terminal, Chatbot folder

`git init`

`git add .`

`git commit -m "v1"`

`heroku creat`

`git push keroku master`

`heroku open`

If the deployment is successful, you will be redirected to a page with "connect" word in it.

## 5.  Find webhook in the facebook developer page

Type the URL that heroku create before

Type the **BOT_TOKEN** in the second block

Choose **message** and **message_postback**

## 6. Well Done, your ChatBot is runing now!
