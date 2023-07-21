const express = require('express');
const mongoose = require('mongoose');
const user = require('./user.handler');
const app = express();
const port = 6969;

app.use(express.json());
mongoose.connect('mongodb+srv://jpalacio:admin@myapp.moukh6p.mongodb.net/api-db?retryWrites=true&w=majority');



app.get('/api/',user.list);
app.post('/api/',user.create);
app.get('/api/:id',user.get);
app.put('/api/:id',user.update);
app.delete('/api/:id',user.delete);

app.listen(port,() => {
    console.log(`El ejemplo se está ejecutando en el puerto ${port}`);
    console.log('run in: http://localhost:6969/api');
});
