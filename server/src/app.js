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





const { Client } = require("pg")
const user = process.argv[2] == "local" ? "goeku" : "goeku"
const password = process.argv[2] == "local" ? undefined : "goeku"
const client = new Client({
    user,
    host: 'localhost',
    database: 'instabot',
    password,
    port: 5432,
});
client.connect();



const initializePassport = require('./passportConfig')
initializePassport(passport);


const app = express()
const PORT = process.env.PORT || 80

// Defining paths for Express config
const publicDirPath = path.join(__dirname, '../public')
const viewsPath = path.join(__dirname, '../templates/views')
const partialsPath = path.join(__dirname, '../templates/partials')

let client_id = null


// Settings for hbs
app.set('view engine', 'hbs')
app.set('views', viewsPath)
hbs.registerPartials(partialsPath)


app.use(express.static(publicDirPath))
app.use(bodyParser.json())

app.use(express.urlencoded({extended: false}));
app.use(
    session({ 
        secret: 'secret',

        resave: false,

        saveUninitialized: false
    })
);

app.use(passport.initialize())
app.use(passport.session())

app.use(flash());


const passwordadm = fs.readFileSync("./password.txt")
// app.use(basicAuth({
//     challenge: true,
//     users: { 'admin': passwordadm.toString() }
// }));



app.get('/', checkAuthenticated, (req, res) => {
    res.render("login")
})

app.get('/bot', checkNotAuthenticated, (req, res) => {
    const runningProcesses = getProcesses(client_id)
    res.render("botindex", runningProcesses)
})

app.get("/clients/register", 
    basicAuth({
        challenge: true,
        users: { 'admin': passwordadm.toString() }
    }), (req, res) => {
    res.render("register");
})

app.get("/clients/login", checkAuthenticated, (req, res) => {
    res.render("login");
})

app.post('/clients/register', async (req, res) =>{
    let { email, password, password2} = req.body;

    console.log({
        email,
        password,
        password2
    });

    let errors = [];

    if (!email || !password || !password2){
        errors.push({message: "Lütfen tüm alanları doldurun."})
    }

    if (password.length < 6){
        errors.push({message: "Şifre en az 6 karakter olmalı."})
    }

    if (password != password2){
        errors.push({message: "Şifre onay aynı değil."})
    }

    if (errors.length > 0){
        res.render('register', {errors})
    }else {
        let hashedPassword = await bcrypt.hash(password, 10);
        console.log(hashedPassword);

        client.query(
            "SELECT * FROM clients WHERE email = $1",
            [email],
            (err, results) => {
                if (err) {
                    throw err;
                }
                console.log(results.rows);

                if (results.rows.length > 0 ){
                    errors.push({message: "Email zaten kayıtlı"});
                    res.render('register', {errors});
                }else{
                    client.query(
                        'INSERT INTO clients (email, password) VALUES ($1, $2) RETURNING id, password', 
                        [email, hashedPassword], 
                        (err, results) => {
                            if (err){
                                throw err
                            }
                            console.log(results.rows);
                            req.flash('success_msg', "Kayıt oldunuz. Giriş yapabilirsiniz.");
                            res.redirect("login");
                        }
                    )
                }
            }
        );
    }
})

app.post("/clients/login", 
    passport.authenticate("local", {
        failureRedirect: "/clients/login",
        failureFlash: true
    }),
    async (req, res) => {
        //console.log("@@@" + req.user.id)
        client_id = req.user.id
        res.redirect('/bot')
    }
);

app.get('/process', checkNotAuthenticated, async (req, res) => {
    const dmProfiles = await databaseUtils.getDmProfiles(client_id)
    const dmProfileNames = Object.keys(dmProfiles)
    res.render("process", { names: dmProfileNames })
})

app.post('/process', (req, res) => {
    res.send({})
    createProcess(req.body, client_id)
})

app.get("/exitProcess/:username", checkNotAuthenticated, (req, res) => {
    exitProcess(req.params.username)
    res.redirect("/")
})

app.get("/reports", checkNotAuthenticated, async (req, res) => {
    const likes = await databaseUtils.getLikes(client_id)
    const requests = await databaseUtils.getRequests(client_id)
    const dm = await databaseUtils.getDm(client_id)
    const blacklist = await databaseUtils.getBlacklist(client_id)

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
    createProcess(req.body, client_id)
})

app.get("/hashtagProcess", checkNotAuthenticated, (req, res) => {
    res.render("hashtagProcess")
})

app.get('/download', async (req, res) => {
    const blacklist = await databaseUtils.getBlacklist(client_id)
    fs.writeFileSync("./blacklist.json", JSON.stringify(blacklist.rows))

    res.download('./blacklist.json')
})

app.get("/settings", checkNotAuthenticated, (req, res) => {
    res.render("settings")
})

app.post("/settings", (req, res) => {
    res.send({})
    fs.writeFileSync("./password.txt", req.body.newPassword)
})

app.get("/hashtag", checkNotAuthenticated, async (req, res) => {
    const users = await databaseUtils.getUsers(client_id)
    res.render("hashtag", { users: users.rows })
})

app.post("/hashtag", async (req, res) => {
    await databaseUtils.removeUser(req.body.username, client_id)
    res.send({})
})

app.get("/downloadUsers", checkNotAuthenticated, async (req, res) => {
    let users = await databaseUtils.getUsers(client_id)
    users = users.rows.map(user => user.account)
    users = users.join('\n')

    fs.writeFileSync("./users.txt", users)

    res.download('./users.txt')
})

app.get("/dmProfile", checkNotAuthenticated, async (req, res) => {
    const profiles = await databaseUtils.getDmProfiles(client_id)
    res.render("dmProfile", { data: profiles })
})

app.get("/createDmProfile", checkNotAuthenticated, async (req, res) => {
    res.render("createDmProfile")
})

app.post("/createDmProfile", async (req, res) => {
    await databaseUtils.addDmProfile(req.body, client_id)
    res.send({})
})

app.get("/summary", checkNotAuthenticated, async (req, res) => {
    const summaries = await databaseUtils.getSummaries(client_id)
    res.render("summary", { summary: summaries.rows })
})

app.get('*', (req, res) => {
    res.send('404')
})


function checkAuthenticated(req, res, next){
    if(req.isAuthenticated()){
        return res.redirect("/bot");
    }
    next();
}

function checkNotAuthenticated(req, res, next){
    if (req.isAuthenticated()){
        return next()
    }
    res.redirect("/clients/login");
}

app.listen(PORT, () => {
    console.log(`Server is up on port ${PORT}`)
})