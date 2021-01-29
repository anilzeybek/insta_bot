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

function getBlacklist() {
    return new Promise((resolve, reject) => {
        db.all("SELECT * FROM blacklist", (err, rows) => {
            if (err) reject(err)
            else resolve(rows)
        })
    })
}

exports.getLikes = getLikes
exports.getRequests = getRequests
exports.getBlacklist = getBlacklist
