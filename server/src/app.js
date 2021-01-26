const path = require('path')
const express = require('express')
const bodyParser = require('body-parser')
const hbs = require('hbs')
const createProcess = require("./createProcess")

const app = express()
const PORT = process.env.PORT || 3000

// Defining paths for Express config
const publicDirPath = path.join(__dirname, '../public')
const viewsPath = path.join(__dirname, '../views')

// Settings for hbs
app.set('view engine', 'hbs')
app.set('views', viewsPath)

app.use(express.static(publicDirPath))
app.use(bodyParser.json())

app.get('/', (req, res) => {
    res.render("index")
})

app.get('/process', (req, res) => {
    // TODO: burda çalışan processleri bul, onları gönder

    const processes = {}
    res.render("process", processes)
})

app.post('/process', (req, res) => {
    res.send({})
    createProcess(req.body)
})

app.get('*', (req, res) => {
    res.send('404')
})

app.listen(PORT, () => {
    console.log(`Server is up on port ${PORT}`)
})