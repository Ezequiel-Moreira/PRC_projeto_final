var createError = require('http-errors') 
var express = require('express') 
var path = require('path') 
var cookieParser = require('cookie-parser') 
var logger = require('morgan') 
const nocache = require('nocache')

//routers
//NOTE: these are all API for the frontend
var homepageRouter = require('./routes/homepage') 

var elementsRouter = require('./routes/elements')

var moleculesRouter = require('./routes/molecules')

// var usersRouter = require('./routes/users') 

var app = express() 

// view engine setup
app.set('views', path.join(__dirname, 'views')) 
app.set('view engine', 'pug') 

app.use(logger('dev')) 

//CORS setup
app.use((req,res,next)=>{
  res.header('Access-Control-Allow-Origin', '*')
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Content-Length, X-Requested-With, Origin, Accept')
  next()
})

//remove cache because of 304 "error"
app.use(nocache())

app.use(express.json()) 
app.use(express.urlencoded({ extended: false })) 
app.use(cookieParser()) 
app.use(express.static(path.join(__dirname, 'public'))) 

//routes
app.use('/api', homepageRouter) 

app.use('/api/elements',elementsRouter)

app.use('/api/molecules',moleculesRouter)


// app.use('/users', usersRouter) 

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404)) 
}) 

// error handler
app.use(function(err, req, res) {
  // set locals, only providing error in development
  res.locals.message = err.message 
  res.locals.error = req.app.get('env') === 'development' ? err : {} 

  // render the error page
  res.status(err.status || 500) 
  res.render('error') 
}) 

module.exports = app 
