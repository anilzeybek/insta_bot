const path = require('path')
const express = require('express')
const bodyParser = require('body-parser')
const hbs = require('hbs')
const { createProcess, getProcesses, exitProcess } = require("./processUtils")
const databaseUtils = require("./databaseUtils")
const basicAuth = require('express-basic-auth')
const fs = require('fs')
const bcrypt = require('bcrypt')
const session = require('express-session')
const flash = require('express-flash')
const passport = require('passport')


const initializePassport = require('./passportConfig')
initializePassport(passport);


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
app.use(bodyParser.urlencoded({ extended: true }));

app.use(
    session({
        secret: 'secret',
    })
);

app.use(passport.initialize())
app.use(passport.session())

app.use(flash());


app.get('/', checkAuthenticated, (req, res) => {
    res.render("login")
})

app.get('/logout', function(req, res){
  req.logout();
  res.redirect('/');
});

app.get('/bot', checkNotAuthenticated, (req, res) => {
    const runningProcesses = getProcesses(req.user.id)
    res.render("botindex", runningProcesses)
})

app.get("/clients/register",
    basicAuth({
        challenge: true,
        users: { 'admin': "GokselAnil1234?" }
    }), (req, res) => {
        res.render("register");
    })

app.get("/clients/login", checkAuthenticated, (req, res) => {
    res.render("login");
})

app.post('/clients/register', async (req, res) => {
    let { email, password, password2 } = req.body;

    console.log({
        email,
        password,
        password2
    });

    let errors = [];

    if (!email || !password || !password2) {
        errors.push({ message: "Lütfen tüm alanları doldurun." })
    }

    if (password.length < 6) {
        errors.push({ message: "Şifre en az 6 karakter olmalı." })
    }

    if (password != password2) {
        errors.push({ message: "Şifre onay aynı değil." })
    }

    if (errors.length > 0) {
        res.render('register', { errors })
    } else {
        let hashedPassword = await bcrypt.hash(password, 10);
        console.log(hashedPassword);

        databaseUtils.registerClient(email, hashedPassword, req, res);
    }
})

app.post("/clients/login",
    passport.authenticate("local", {
        successRedirect: "/bot",
        failureRedirect: "/clients/login",
        failureFlash: true
    })
);

app.get('/process', checkNotAuthenticated, async (req, res) => {
    const dmProfiles = await databaseUtils.getDmProfiles(req.user.id)
    const dmProfileNames = Object.keys(dmProfiles)
    res.render("process", { names: dmProfileNames })
})

app.post('/process', (req, res) => {
    res.send({})
    createProcess(req.body, req.user.id)
})

app.get("/exitProcess/:username", checkNotAuthenticated, (req, res) => {
    exitProcess(req.params.username)
    res.redirect("/")
})

app.get("/reports", checkNotAuthenticated, async (req, res) => {
    const likes = await databaseUtils.getLikes(req.user.id)
    const requests = await databaseUtils.getRequests(req.user.id)
    const dm = await databaseUtils.getDm(req.user.id)
    const blacklist = await databaseUtils.getBlacklist(req.user.id)

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

app.get("/requests", checkNotAuthenticated, (req, res) => {
    res.render("requests")
})

app.post('/requests', (req, res) => {
    res.send({})
    createProcess(req.body, req.user.id)
})

app.get("/hashtagProcess", checkNotAuthenticated, (req, res) => {
    res.render("hashtagProcess")
})

app.get('/download', async (req, res) => {
    const blacklist = await databaseUtils.getBlacklist(req.user.id)
    fs.writeFileSync("./blacklist.json", JSON.stringify(blacklist.rows))

    res.download('./blacklist.json')
})

// app.post("/settings", (req, res) => {
//     res.send({})
//     fs.writeFileSync("./password.txt", req.body.newPassword)
// })

app.get("/hashtag", checkNotAuthenticated, async (req, res) => {
    const users = await databaseUtils.getUsers(req.user.id)
    res.render("hashtag", { users: users.rows })
})

app.post("/hashtag", async (req, res) => {
    await databaseUtils.removeUser(req.body.username, req.user.id)
    res.send({})
})

app.get("/downloadUsers", checkNotAuthenticated, async (req, res) => {
    let users = await databaseUtils.getUsers(req.user.id)
    users = users.rows.map(user => user.account)
    users = users.join('\n')

    fs.writeFileSync("./users.txt", users)

    res.download('./users.txt')
})

app.get("/dmProfile", checkNotAuthenticated, async (req, res) => {
    const profiles = await databaseUtils.getDmProfiles(req.user.id)
    res.render("dmProfile", { data: profiles })
})

app.get("/createDmProfile", checkNotAuthenticated, async (req, res) => {
    res.render("createDmProfile")
})

app.post("/createDmProfile", async (req, res) => {
    await databaseUtils.addDmProfile(req.body, req.user.id)
    res.send({})
})

app.get("/summary", checkNotAuthenticated, async (req, res) => {
    const summaries = await databaseUtils.getSummaries(req.user.id)
    res.render("summary", { summary: summaries.rows })
})

app.get('*', (req, res) => {
    res.send('404')
})


function checkAuthenticated(req, res, next) {
    if (req.isAuthenticated()) {
        return res.redirect("/bot");
    }
    next();
}

function checkNotAuthenticated(req, res, next) {
    if (req.isAuthenticated()) {
        return next()
    }
    res.redirect("/clients/login");
}

app.listen(PORT, () => {
    console.log(`Server is up on port ${PORT}`)
})
