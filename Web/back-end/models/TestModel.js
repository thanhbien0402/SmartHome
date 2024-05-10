const mongoose = require('mongoose')

const TestSchema = new mongoose.Schema({
    id: String,
    value: Number,
    feed_id: Number,
    feed_key: String,
    created_at: Date,
})

module.exports = mongoose.model('Test', TestSchema, 'test')