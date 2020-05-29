# naywee-orbital-20
Team Naywee's Orbital 20 Project

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

