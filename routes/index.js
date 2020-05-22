var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'NMTB Admin', test:'Test'});
});

router.post('/post', function(req, res, next) {
  console.log('Got body:', req.body);
  res.render('index', { title: 'NMTB Admin', test:req.body.test});
});

/* GET settings page. */
router.get('/settings', function(req, res, next) {
  res.render('settings', { title: 'NMTB Admin'});
});

/* GET help page. */
router.get('/help', function(req, res, next) {
  res.render('help', { title: 'NMTB Admin'});
});

/* GET login page. */
router.get('/login', function(req, res, next) {
  res.render('login', { title: 'NMTB Admin'});
});

/* GET contact page. */
router.get('/contact', function(req, res, next) {
  res.render('contact', { title: 'NMTB Admin'});
});

module.exports = router;
