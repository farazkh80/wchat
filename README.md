# WCHAT
WChat is a multi-socket group chat app, developed with <b>Python's Flask</b> framework and modules on the backend as well as pure <b>JavaScript</b>  and a responsive <b>Bootstrap</b> design on the frontend.


## Link to heroku live app

https://rchat-app80.herokuapp.com/


## Configuration
 
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
On your project folder enter the following commands in order to create a virtual environment.

```bash
virtualenv venv
```

Next, activate your virtual environment using the following command.

```bash
vev/Scripts/activate
```

Install the requirements using the following command.

```bash
pip install -r requirements.txt
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

## Running

To run your project enter the following command.

```
python application.py
```


You will be directed to a registration page first.

![Registration Page](/visuals/reg-page.PNG)


After completing the registration you will be required to login with your credentials.

![Login Page](/visuals/login-page.PNG)


Upon logging in, you will be able to use different chat rooms to talk with the online users.

![Chat Room](/visuals/chat-room.PNG)



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.



## Future Improvements

1- The main future goal is to connect WChat to a MongoDB database in order save previous messages.

2- Another possible feature is offering users a way to connect with other users through unique username search. 

## License

[MIT](https://choosealicense.com/licenses/mit/)



