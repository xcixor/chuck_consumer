# chuck_consumer

This simple app retrieves categories from the [chucknorris.io api](https://api.chucknorris.io/), displays them and their content.


## Development
### Prerequisites
- Docker - ensure you have docker installed in your machine to ease development.

- To deploy the application run the command `make dev` or `docker-compose up --build --force-recreate --remove-orphans --detach` and navigate to http://0.0.0.0:8000/ on your browser to view the app locally.
- To test the app run the command make test or `docker-compose run chuck-consumer coverage run --rcfile=.coveragerc manage.py test`

You can also check out the [deployed version](https://chuck-consumer.herokuapp.com/)