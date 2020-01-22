# Text Analysis API app

Web application that consume the restful API of Comic Vine which is the largest comic database online.

Features:
-   Show a list of the last comics
    
-   Show a detail of the selected comic

## Prerequisites
This app was set with python 3.5, so you have to make sure that you have python3 installed in your machine.

It's better to set a virtual environment. To do that first install virtualenv:

    $ pip install virtualenv
    
 then we are going to create the virtualenv to run the app, please ru the following commands in your terminal:
 
    $ mkdir myvirtualEnvs && cd myvirtualEnvs
    $ virtualenv textAnalysisEnv -p $(which python3)
    $ cd
    

## Getting started

First clone this repository:

    $ git clone https://github.com/Noeuclides/WhaleandJaguarWeb.git

then go to the repo's directory:

    $ cd WhaleandJaguarWeb
    $ source ../myvirtualEnvs/textAnalysisEnv/bin/activate    

There you can install all the prerequisites to run the app in your computer:

    $ pip install -r requirements.txt

Before run the application you’ll need to grab an API Key, you can do that in the following link:
https://developer.aylien.com/signup

There you can install all the prerequisites to run the app in your computer:

    $ cd WandJ_Web/apps/textAnalysis

Open the credentials.py file in your text editor and put your ID and KEY from the aylien page in the corresponding fields(inside the quotes):

     credentials = {
        'id': 'YOUR_ID',
        'key': 'YOUR_KEY'
     }


## Run the App

Now you can run the app easily. In the application folder run the following command. You must be in ~/WhaleandJaguarWeb/WandJ_Web/ path (make sure you have the file 'manage.py' in the current directory):

    $ python manage.py runserver

If everything goes well, you should see something like this:

    (WandJDjangoEnv) λ ~/WhaleandJaguarWeb/WandJ_Web/ master* python manage.py runserver
     Watching for file changes with StatReloader
     Performing system checks...
     
     System check identified no issues (0 silenced).
     January 22, 2020 - 09:48:08
     Django version 2.2.9, using settings 'WandJ_Web.settings'
     Starting development server at http://127.0.0.1:8000/
     Quit the server with CONTROL-C.


go to your browser and write "http://127.0.0.1:8000/", to view the wap page.





