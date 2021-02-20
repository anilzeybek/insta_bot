const sqlite3 = require("sqlite3").verbose()

const db = new sqlite3.Database('../database.db', (err) => {
    if (err) console.error(err.message);
    console.log('Connected to database.');
});

function getLikes() {
    return new Promise((resolve, reject) => {
        db.all("SELECT * FROM likes", (err, rows) => {
            if (err) reject(err)
            else resolve(rows)
        })
    })
}

function getRequests() {
    return new Promise((resolve, reject) => {
        db.all("SELECT * FROM follow_requests", (err, rows) => {
            if (err) reject(err)
            else resolve(rows)
        })
    })
}

function getDm() {
    return new Promise((resolve, reject) => {
        db.all("SELECT * FROM dm", (err, rows) => {
            if (err) reject(err)
            else resolve(rows)
        })
    })
}

function getBlacklist() {
    return new Promise((resolve, reject) => {
        db.all("SELECT * FROM blacklist", (err, rows) => {
            if (err) reject(err)
            else resolve(rows)
        })
    })
}

function getUsers() {
    return new Promise((resolve, reject) => {
        db.all("SELECT * FROM users", (err, rows) => {
            if (err) reject(err)
            else resolve(rows)
        })
    })
}

function removeUser(username) {
    return new Promise((resolve, reject) => {
        db.run(`DELETE FROM users WHERE account=?`, username, err => {
            if (err) reject(err)
            else resolve()
        })
    })
}

exports.getLikes = getLikes
exports.getRequests = getRequests
exports.getDm = getDm
exports.getBlacklist = getBlacklist
exports.getUsers = getUsers
exports.removeUser = removeUser