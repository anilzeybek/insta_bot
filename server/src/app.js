const path = require('path')
const express = require('express')
const bodyParser = require('body-parser')
const hbs = require('hbs')
const {createProcess, getProcesses, exitProcess} = require("./processUtil")

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
    const runningProcesses = getProcesses()
    res.render("index", runningProcesses)
})

app.get('/process', (req, res) => {
    res.render("process")
})

app.post('/process', (req, res) => {
    res.send({})
    createProcess(req.body)
})

app.get("/exitProcess/:username", (req, res) => {
    exitProcess(req.params.username)
    res.redirect("/")
})

app.get('*', (req, res) => {
    res.send('404')
})

app.listen(PORT, () => {
    console.log(`Server is up on port ${PORT}`)
})