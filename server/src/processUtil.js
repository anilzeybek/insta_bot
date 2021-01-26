const fs = require('fs');

const workingUsernames = []
let runningProcesses = []

function createProcess(data) {
    fs.writeFileSync("../options.json", JSON.stringify(data))

    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python3', ["../bot/create_process.py", "options.json"]);

    workingUsernames.push(data.username)
    runningProcesses.push({
        username: data.username,
        process: pythonProcess
    })

    pythonProcess.stdout.on('data', data => {
        console.log(data.toString())
    })

    pythonProcess.stderr.on('data', data => {
        console.log(data.toString())
    })

    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`)

        const index = workingUsernames.indexOf(data.username)
        if (index !== -1)
            workingUsernames.splice(index, 1)
    })
}

function getProcesses() {
    return {usernames: workingUsernames}
}

function exitProcess(username) {
    for (const runningProcess of runningProcesses) {
        if (runningProcess.username === username) {
            runningProcess.process.kill("SIGKILL")

            const index = workingUsernames.indexOf(username)
            if (index !== -1)
                workingUsernames.splice(index, 1)

            runningProcesses = runningProcesses.filter(function (obj) {
                return obj.username !== username;
            });

            break
        }
    }
}

exports.createProcess = createProcess
exports.getProcesses = getProcesses
exports.exitProcess = exitProcess
