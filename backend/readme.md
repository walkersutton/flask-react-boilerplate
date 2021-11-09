# Backend README

# TODO
* lint

# how to initialize the environemtn
* python3 -m venv venv
* soruce venv/bin/activate
* pip install -r requirements.txt **double check nothing extra**
# how to run the backend server
## option 1:
* source venv/bin/activate
* python server.py
## option 2:
* export FLASK_ENV=server.py **need to confirm this is correct syntax, haven't tried**
* flask run
### details about env variables to set for running debug mode, updating changes, etc...


# build database schema from models
will probably want to add some sort of migration script, but not now
``` python
from server import engine
from models import Base
Base.metadata.create_all(engine)
```

