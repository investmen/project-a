# project-a

1. virtualenv --python=python3 ompvenv
2. cd ompvenv/
3. source bin/activate
4. pip install django
5. django-admin --version
2.1.4
6. cd ompsite/
7. python manage.py runserver
8. Access the report app at http://127.0.0.1:8000/report/



# Environment Setup using Anaconda / Spyder
Access the report app at http://127.0.0.1:8000/report/
1. create a virtual environment from conda terminal 
    conda create -n ompvenv python=3.7 anaconda
2. activate the virtual environment
    activate ompvenv
3. install django to the virtual environment
    conda install -c anaconda django 
4. clone the git repository 'project a' to your local folder
5. navigate to that local folder in conda terminal and run the server
      python manage.py runserver
6. Access the report app at http://127.0.0.1:8000/report/