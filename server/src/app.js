const path = require('path')
const express = require('express')
const bodyParser = require('body-parser')
const hbs = require('hbs')
const { createProcess, getProcesses, exitProcess } = require("./processUtils")
const databaseUtils = require("./databaseUtils")
const basicAuth = require('express-basic-auth')
const fs = require('fs')


const app = express()
const PORT = process.env.PORT || 3000

// Defining paths for Express config
const publicDirPath = path.join(__dirname, '../public')
const viewsPath = path.join(__dirname, '../templates/views')
const partialsPath = path.join(__dirname, '../templates/partials')


// Settings for hbs
app.set('view engine', 'hbs')
app.set('views', viewsPath)
hbs.registerPartials(partialsPath)


app.use(express.static(publicDirPath))
app.use(bodyParser.json())

const password = fs.readFileSync("./password.txt")
app.use(basicAuth({
    challenge: true,
    users: { 'admin': password.toString() }
}));


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

app.get("/reports", async (req, res) => {
    const likes = await databaseUtils.getLikes()
    const requests = await databaseUtils.getRequests()
    const dm = await databaseUtils.getDm()
    const blacklist = await databaseUtils.getBlacklist()

    const data = {
        likes: likes.rows,
        likesLength: likes.rows.length,
        requests: requests.rows,
        requestsLength: requests.rows.length,
        dm: dm.rows,
        dmLength: dm.rows.length,
        blacklist: blacklist.rows,
        blacklistLength: blacklist.rows.length
    }

    res.render("reports", data)
})

app.get("/requests", (req, res) => {
    res.render("requests")
})

app.post('/requests', (req, res) => {
    res.send({})
    createProcess(req.body)
})

app.get('/download', async (req, res) => {
    const blacklist = await databaseUtils.getBlacklist()
    fs.writeFileSync("./blacklist.json", JSON.stringify(blacklist.rows))

    res.download('./blacklist.json')
})

app.get("/settings", (req, res) => {
    res.render("settings")
})

app.post("/settings", (req, res) => {
    res.send({})
    fs.writeFileSync("./password.txt", req.body.newPassword)
})

app.get("/hashtag", async (req, res) => {
    const users = await databaseUtils.getUsers()
    res.render("hashtag", { users: users.rows })
})

app.post("/hashtag", async (req, res) => {
    await databaseUtils.removeUser(req.body.username)
    res.send({})
})

app.get("/downloadUsers", async (req, res) => {
    let users = await databaseUtils.getUsers()
    users = users.rows.map(user => user.account)
    users = users.join('\n')

    fs.writeFileSync("./users.txt", users)

    res.download('./users.txt')
})

app.get("/dmProfile", async (req, res) => {
    const profiles = await databaseUtils.getDmProfiles()
    res.render("dmProfile", profiles)
})

app.get("/createDmProfile", async (req, res) => {
    res.render("createDmProfile")
})

app.post("/createDmProfile", async (req, res) => {
    await databaseUtils.addDmProfile(req.body.data)
    res.send({})
})

app.get('*', (req, res) => {
    res.send('404')
})

app.listen(PORT, () => {
    console.log(`Server is up on port ${PORT}`)
})