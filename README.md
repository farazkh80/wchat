#  WCHAT

## Link to heroku live app

https://rchat-app80.herokuapp.com/

## How to run on a local system
 
First navigate through the terminal to this projects folder
and enter the following command
```
$ python get-pip.py
```
Then make sure all the required modules listed iin requirements.txt file are installed on your machine.
For manual installation enter the following command.
```
$ pip3 install moduleName
```
Make sure that you have install virtual environment, if not use the following command
```
$ pip3 install virtualenv
```
On your project folder enter the following commands in order to activate you venv.
```
$ virtualenv env
```

```
$ \path\to\env\Scripts\activate
```
Make a few adjustment on the code at application.py file:

1- Change the database secret key and url according to their comments above of them (can be found from line 10 to 17 on application.py)
```python
# actual secret key if running on a local system => "b'0\x17\xdb\x03\xdc\x0c;ja\xecv\xb0a\xe9$\x13'"
app.secret_key = app.secret_key = os.environ.get("SECRET")


# configure database
# Actual Database url if running on a local system => "postgres://xwawslekazwoni:ba0ee8e746269e7cc8ff5804aa28c3205e0309757bb2673ffad22d793bb13b92@ec2-34-225-162-157.compute-1.amazonaws.com:5432/dcqg3bakntjhp"
app.config[
    'SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
```

2- Change the last line of code on application.py according to the guide below.
```python
# remove the code below and use "socketio.run(app, debug=True)" if running on a local system
app.run()
```

Finally to run your project enter the following command.
```
$ python application.py
```

## Some Visuals from WCHAT app platform

Registration Page

![Registration Page](https://github.com/farazkh80/wchat/blob/master/visuals/reg-page.PNG)

Login Page

![Login Page](https://github.com/farazkh80/wchat/blob/master/visuals/login-page.PNG)

Chat Room

![Chat Room](https://github.com/farazkh80/wchat/blob/master/visuals/chat-room.PNG)

