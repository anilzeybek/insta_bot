const { Client } = require("pg")

//require("dotenv").config();



const user = process.argv[2] == "local" ? "anilzeybek" : "postgres"
const password = process.argv[2] == "local" ? undefined : "postgres"
const client = new Client({
    user,
    host: 'localhost',
    database: 'instabot',
    password,
    port: 5432,
});
client.connect();


async function getLikes(client_id) {
    try {
        const res = await client.query(`SELECT * FROM likes WHERE client_id='${client_id}'`);
        return res;
    } catch (err) {
        console.log(err.stack);
    }
}

async function getRequests(client_id) {
    try {
        const res = await client.query(`SELECT * FROM follow_requests WHERE client_id='${client_id}'`);
        return res;
    } catch (err) {
        console.log(err.stack);
    }
}

async function getDm(client_id) {
    try {
        const res = await client.query(`SELECT * FROM dm WHERE client_id='${client_id}'`);
        return res;
    } catch (err) {
        console.log(err.stack);
    }
}

async function getBlacklist(client_id) {
    try {
        const res = await client.query(`SELECT * FROM blacklist WHERE client_id='${client_id}'`);
        return res;
    } catch (err) {
        console.log(err.stack);
    }
}

async function getUsers(client_id) {
    try {
        const res = await client.query(`SELECT * FROM users WHERE client_id='${client_id}'`);
        return res;
    } catch (err) {
        console.log(err.stack);
    }
}

async function removeUser(username, client_id) {
    await client.query(`DELETE FROM users WHERE account='${username}' AND client_id='${client_id}'`)
}

async function getDmProfiles(client_id) {
    try {
        const res = await client.query(`SELECT * FROM dm_profiles WHERE client_id='${client_id}'`)

        const result = {}
        res.rows.forEach(row => {
            if (!(row.profile_name in result)) {
                result[row.profile_name] = [row.dm_message]
            } else {
                result[row.profile_name].push(row.dm_message)
            }
        })

        return result
    } catch (err) {
        console.log(err.stack);
    }
}

async function addDmProfile(profile, client_id) {
    for (const message of profile.messages) {
        await client.query(`INSERT INTO dm_profiles(profile_name, dm_message, client_id) VALUES('${profile.profileName}', '${message}', ${client_id})`)
    }
}

async function getSummaries(client_id) {
    try {
        const res = await client.query(`SELECT * FROM summary WHERE client_id='${client_id}'`)
        return res
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
exports.addDmProfile = addDmProfile
exports.getSummaries = getSummaries