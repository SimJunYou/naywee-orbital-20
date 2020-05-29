var express = require('express');
var router = express.Router();

/* DATABASE POOL */
const { pool } = require('./db')

//create a test entry

router.post("/", async (req, res) => {
  try {
    const { description } = req.body;
    const newTodo = await pool.query(
      "INSERT INTO test (description) VALUES($1) RETURNING *",
      [description]
    );

    res.json(newTodo.rows[0]);
  } catch (err) {
    console.error(err.message);
  }
});

//get all test entries

router.get("/", async (req, res) => {
  try {
    const allTodos = await pool.query("SELECT * FROM test");
    res.json(allTodos.rows);
  } catch (err) {
    console.error(err.message);
  }
});

//get a test entry

router.get("/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const todo = await pool.query("SELECT * FROM test WHERE id = $1", [
      id
    ]);

    res.json(todo.rows[0]);
  } catch (err) {
    console.error(err.message);
  }
});

//delete a test entry

router.delete("/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const deleteTodo = await pool.query("DELETE FROM test WHERE id = $1", [
      id
    ]);
    res.json(true);
  } catch (err) {
    console.log(err.message);
    res.json(false);
  }
});

module.exports = router;
