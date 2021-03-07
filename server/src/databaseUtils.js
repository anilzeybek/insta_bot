const {Client} = require("pg")
const client = new Client({
    // user: 'postgres',
    user: 'anilzeybek',
    host: 'localhost',
    database: 'instabot',
    // password: 'postgres',
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

async function getDmProfiles() {
    try {
        const res = await client.query(`SELECT * FROM dm_profiles`)

        const result = {}
        res.rows.forEach(row => {
            if (row[0] in result)  {
                result[row[0]] = [row[1]]
            } else {
                result[row[0]].push(row[1])
            }
        })

        return result
    } catch (err) {
        console.log(err.stack);
    }
}

exports.getLikes = getLikes
exports.getRequests = getRequests
exports.getDm = getDm
exports.getBlacklist = getBlacklist
exports.getUsers = getUsers
exports.removeUser = removeUser
exports.getDmProfiles = getDmProfiles