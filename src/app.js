const express = require('express');
const path = require('path');

//Set up public path
const publicPath = path.resolve(__dirname, 'public/');

//Create app
const app = express();

// Bring in handlebars for templating
app.set('view engine', 'hbs');

// Set up middleware
app.use(express.urlencoded({ extended: false }));
app.use(express.static(publicPath));

app.get('/', (req, res) => {
    res.render('homeLayout', {homeActive: 'active'});
});

app.get('/app', (req, res) => {

});

app.get('/demo', (req, res) => {
    res.render('demoLayout', {demoActive: 'active'});
});

app.post('/demo', (req, res) => {
    const spawn = require('child_process').spawn;
    const process = spawn('python', [__dirname + '\\main.py', req.body.fileName]);

    process.stdout.on('data', (data) => {
        const result = data.toString();
        if (result === "success") {
            res.render('demoLayout', {message: "Upload failed"});
        } else {
            res.render('demoLayout', {message: "Upload success"});
        }
    });
    //res.redirect('/');
});

app.listen(3000);
