How to run?

Get all files somewhere - then being in directory containing project run this command:

source auth/bin/activate

Then to install all dependencies run command:

npm install

It should handle all required dependencies. Now you should run:

export FLASK_APP=__init__.py

And then

flask run

Application should start under your localhost / 127.0.0.1 address with port 5000.