var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var cors = require("cors");
// var createError = require('http-errors');

/* ROUTING */
var indexRouter = require('./src/index');
var usersRouter = require('./src/users');

var app = express();

app.use(logger('dev'));
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());

if (process.env.NODE_ENV === "production") {
    // server static content
    // 'npm run build'
    app.use(express.static(path.join(__dirname, "client/build")));
}

// basic routes
app.use('/', indexRouter);
app.use('/users', usersRouter);

// catch everything else and send to index.html
app.get("*", (req, res) => {
    res.sendFile(path.join(__dirname, "client/build/index.html"));
});

// // catch 404 and forward to error handler
// app.use(function(req, res, next) {
//   next(createError(404));
// });

// // error handler
// app.use(function(err, req, res, next) {
//   // set locals, only providing error in development
//   res.locals.message = err.message;
//   res.locals.error = req.app.get('env') === 'development' ? err : {};

//   console.log(err.message)

//   // render the error page
//   res.status(err.status || 500);
//   res.render('error');
// });

module.exports = app;
