// This is a simple hello world program that uses express to create a server and listens on port 3000.
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello NodeJs!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})