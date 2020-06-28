var express = require('express');
var router = express.Router();

/* DATABASE POOL */
const { pool } = require('./db')

// Create a new student
// - s_id (text) (the telegram ID)
// - full_name (the full name from Telegram)
router.post("/api/students/sync", async (req, res) => {
  try {
    const { s_id, full_name, lessons } = req.body;

    const newStudent = await pool.query(
      `
      INSERT INTO students VALUES ($1, $2) ON CONFLICT (s_id)
      DO UPDATE
        full_name=EXCLUDED.full_name
      RETURNING *;
      `,
      [s_id, full_name]
    );

    const response = [newStudent.rows[0]];

    // lessons:
    //   { lesson1, lesson2, lesson3, etc...}
    // lessonX:
    //   { l_id, days, periods, venues }

    var lessonX = {};
    while (Object.keys(lessons).length === 0) {
      let { lessonX, ...lessons } = lessons;
      const { l_id, days, periods, venues } = lessonX;

      const newLesson = await pool.query(
        `
        INSERT INTO lessons VALUES($1, $2, $3, $4) ON CONFLICT (l_id)
        DO UPDATE SET
          days=EXCLUDED.days,
          periods=EXCLUDED.periods,
          venues=EXCLUDED.venues
        RETURNING *;
        `,
        [l_id, days, periods, venues]
      );

      response.push(newLesson.rows[0]);
    };

    res.json(response);
  } catch (err) {
    console.error(err.message);
  }
});

// Get all students
router.get("/api/students", async (req, res) => {
  try {
    const allTodos = await pool.query("SELECT * FROM students");
    res.json(allTodos.rows);
  } catch (err) {
    console.error(err.message);
  }
});

//Get one student entry based on s_id
router.get("/api/students/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const todo = await pool.query("SELECT * FROM students WHERE s_id = $1", [
      id
    ]);

    res.json(todo.rows[0]);
  } catch (err) {
    console.error(err.message);
  }
});

//Delete student entry based on s_id
router.delete("/api/students/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const deleteTodo = await pool.query("DELETE FROM students WHERE s_id = $1", [
      id
    ]);
    res.json(true);
  } catch (err) {
    console.log(err.message);
    res.json(false);
  }
});

// LESSONS ////////////////////////////////////////////////////////

// Create a new lesson
// - l_id (text) (e.g. 'CS1232S=LEC:1')
// - days (text) (e.g. 'WED, FRI')
// - periods (text) (e.g. '1000-1200, 1000-1100')
// - venues (text) (e.g. 'UT-AUD2, UT_AUD2')
router.post("/api/lessons", async (req, res) => {
  try {
    const { l_id, days, periods, venues } = req.body;
    const newTodo = await pool.query(
      "INSERT INTO lessons VALUES($1, $2, $3, $4) RETURNING *",
      [l_id, days, periods, venues]
    );

    res.json(newTodo.rows[0]);
  } catch (err) {
    console.error(err.message);
  }
});

// Get all lessons
router.get("/api/lessons", async (req, res) => {
  try {
    const allTodos = await pool.query("SELECT * FROM lessons");
    res.json(allTodos.rows);
  } catch (err) {
    console.error(err.message);
  }
});

//Get one lesson entry based on s_id
router.get("/api/lessons/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const todo = await pool.query("SELECT * FROM lessons WHERE l_id = $1", [
      id
    ]);

    res.json(todo.rows[0]);
  } catch (err) {
    console.error(err.message);
  }
});

//Delete student entry based on s_id
router.delete("/api/lessons/:id", async (req, res) => {
  try {
    const { id } = req.params;
    const deleteTodo = await pool.query("DELETE FROM lessons WHERE l_id = $1", [
      id
    ]);
    res.json(true);
  } catch (err) {
    console.log(err.message);
    res.json(false);
  }
});


module.exports = router;
