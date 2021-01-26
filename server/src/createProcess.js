const fs = require('fs');

function createProcess(data) {
    fs.writeFileSync("../options.json", JSON.stringify(data))

    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python3', ["../bot/create_process.py", "options.json"]);

    pythonProcess.stdout.on('data', data => {
        console.log(data.toString())
    })

    pythonProcess.stderr.on('data', data => {
        console.log(data.toString())
    })


    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });
}

module.exports = createProcess