const mongoose = require('mongoose');

const Users = mongoose.model('User',{
    name: { type: String,required: true },
    lastname: { type: String,required: true },
});

module.exports = Users;
