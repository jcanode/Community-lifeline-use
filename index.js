const express = require('express')
// const mongose = require('mongose')
const port = 3001
const app = express()

app.get('/', (req, res) => res.send('Hello azhack!'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
