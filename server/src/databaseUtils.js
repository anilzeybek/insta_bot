const {Client} = require("pg")
const client = new Client({
    user: 'postgres',
    host: 'localhost',
    database: 'instabot',
    password: 'postgres',
    port: 5432,
});
client.connect();


async function getLikes() {
    try {
        const res = await client.query("SELECT * FROM likes");
        return res;
    } catch (err) {
        console.log(err.stack);
    }
}

async function getRequests() {
    try {
        const res = await client.query("SELECT * FROM follow_requests");
        return res;
    } catch (err) {
        console.log(err.stack);
    }
}

async function getDm() {
    try {
        const res = await client.query("SELECT * FROM dm");
        return res;
    } catch (err) {
        console.log(err.stack);
    }
}

async function getBlacklist() {
    try {
        const res = await client.query("SELECT * FROM blacklist");
        return res;
    } catch (err) {
        console.log(err.stack);
    }
}

async function getUsers() {
    try {
        const res = await client.query("SELECT * FROM users");
        return res;
    } catch (err) {
        console.log(err.stack);
    }
}

async function removeUser(username) {
    await client.query(`DELETE FROM users WHERE account=${username}`)
}

exports.getLikes = getLikes
exports.getRequests = getRequests
exports.getDm = getDm
exports.getBlacklist = getBlacklist
exports.getUsers = getUsers
exports.removeUser = removeUser