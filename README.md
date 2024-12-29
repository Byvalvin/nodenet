# NodeNet - By Team Scripted
**Note: This is a copy of the original repo of the project since the CMPUT404 organization deleted the original.**\
Welcome to NodeNet! This web application allows users to sign up, log in, post images, and make friends. 
It provides a platform for users to connect and share moments with their friends and followers.
This project was a part of CMPUT 404: Web Applications and Architecture and was based on Social Distribution. 

- [Deployed website OLD](https://node-net-46d70235bc29.herokuapp.com/nodenet/login/?next=/nodenet/)
- [Project requirements](https://github.com/uofa-cmput404/project-socialdistribution/blob/master/project.org)

- [RE-Deployed website](https://nodenet-fb7f.onrender.com)
  *1-2 mins load up time*
  
## Contributors / Licensing

Authors:

- Albert Dinh
- Dhruvraj Singh
- Mobashhir Khan
- Daniel Asimiakwini
- Jaspreet Singh Dhami

Generally everything is LICENSE'D under the MIT License by Scripted.

## Running instructions

- Set up a virtual environment through these steps:
  - `virtualenv venv --python=python3.8`
  - `source venv/bin/activate`
  - `pip install -r requirements.txt`
- Run the server with `python manage.py runserver`
- Make migrations with the following commands:
  - `python manage.py makemigrations`
  - `python manage.py migrate`

## Useful resources

- [Django Testing](https://docs.djangoproject.com/en/4.2/topics/testing/)
- [Checkout to a git checkout _commit id_ .](https://medium.com/swlh/using-git-how-to-go-back-to-a-previous-commit-8579ccc8180f#:~:text=Go%20back%20to%20the,make%20will%20be%20lost.)
- Get all remote GitHub branches: `git fetch --all`
- Delete a local branch using git: `git branch -d <branch_name>`

## Technologies used

- Bootstrap and CSS for the frontend
- Django for the backend
