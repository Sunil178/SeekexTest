var express = require('express');
const http = require("http");
var path = require('path');
var bodyParser = require('body-parser');
var bucket_controller = require('./controllers/bucket_controller');

var app = express();
var server = require('http').Server(app);

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, 'assets')));

app.get('/', bucket_controller.index);

server.listen(3000)
