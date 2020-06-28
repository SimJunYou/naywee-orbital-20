require('dotenv').config()

const { Pool } = require('pg')
const isProduction = process.env.NODE_ENV === 'production'

//const connectionString = `postgresql://${process.env.DB_USER}:${process.env.DB_PASSWORD}@${process.env.DB_HOST}:${process.env.DB_PORT}/${process.env.DB_DATABASE}`
const connectionString = `postgres://vztlzpweubgkfj:7ac426a262eda6240a9aa9e55d1620244b0f2b7b80e167db4c2e15bd670b63f5@ec2-34-192-173-173.compute-1.amazonaws.com:5432/d4u96tksf79i9l`

const pool = new Pool({
  connectionString: isProduction ? process.env.DATABASE_URL : connectionString,
  ssl: {
    rejectUnauthorized: false
  }
})

module.exports = { pool }