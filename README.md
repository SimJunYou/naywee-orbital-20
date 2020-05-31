# naywee-orbital-20
Team Naywee's Orbital 20 Project

## WEBSITE BRANCH

### Structure

The `client` folder is for the React frontend, which serves as the interface for our website.
The rest of the files and folders in here is for the Express backend, which serves as the REStful API that the frontend uses to perform CRUD operations in our Heroku Postgres database.

### Deploying

This branch is pushed manually onto the Heroku remote repo where the Heroku app is launched from. The Express server will be built and launched first, followed by the React server using the heroku-postbuild script.

## WEBSITE BRANCH - EXPRESS

The Express backend basically only uses [node-pg](https://node-postgres.com/) to make a RESTful API for the React frontend and the Telegram bot.

### API Methods

All test entries are in following format: (`{id: id, description: description}`)

Uses the following HTTP methods:
* `GET: /` - Returns JSON of all test IDs. 
* `GET: /{id}` - Returns JSON of that ID.
* `POST: /` - In body, send JSON of new entry with only `description` (ID is automatically added)
* `DELETE: /{id}` - Returns JSON `{true}` or `{false}` depending on success

### Database Schema

To be decided! 

Only one table (`test`) in one database (`nmtb`) is being used right now.

For test entries, the schema is as follows:
`id: SERIAL PRIMARY KEY`, `description: VARCHAR (255)`
