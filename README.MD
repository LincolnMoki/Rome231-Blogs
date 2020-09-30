# Blogpost

## Author

RonnyLincoln

# Description

This is an application that allows users to sign in or sign up and post blogs.

## User Story

- Comment on the different posts py other uses.
- See the  posts by other uses.
- Vote on posts they have viewed by giving it a upvote or a downvote.
- Register to be allowed to log in to the application
- View posts from the different categories.
- Submit a post to a specific category of their choice.

## BDD

| Behaviour             |                Input                |                                                                       Output |
| :-------------------- | :---------------------------------: | ---------------------------------------------------------------------------: |
| Load the page         |          **On page load**           |                               Get all posts, Select between signup and login |
| Select SignUp         | **Email**,**Username**,**Password** |                                                            Redirect to login |
| Select Login          |    **Username** and **password**    | Redirect to page with app posts based on categories and commenting section |
| Select comment button |             **Comment**             |                                             Form that you input your comment |
| Click on submit       |                                     |       Redirect to all comments tamplate with your comment and other comments |

## Development Installation

To get the code..

1. Cloning the repository:

```bash
https://github.com/ronnylincoln/rome231blog
```

2. Move to the folder and install requirements

```bash
cd blog
pip install -r requirements.txt
```

3. Exporting Configurations

```bash
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
```

4. Running the application

```bash
python3.8 app.py server
```

Open the application on your browser `127.0.0.1:5000`.

## Technology used

- [Python3.8](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Heroku](https://heroku.com)

## Contact Information

dennismwaniki67@gmail.com

## Live Link To Project
https://firewood.herokuapp.com/





## License
  RonnyLincoln@2020
 Licensed under[MIT license](license)

