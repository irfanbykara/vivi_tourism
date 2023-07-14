# Dockerized Django Villa Reservation App
**This project is developed for a tourism company in Turkey as they needed an app to manage their reservations for their flats&villas. Can be used as a base in need of similar web apps.**


# Create your .env file in the main directory. You can take a look at .env.sample file to see what should be the contents of .env file. 

## To build the container

```
docker-compose -f docker-compose-deploy.yml build
```

## To run the container in detached mode

```
docker-compose -f docker-compose-deploy.yml up -d
```
