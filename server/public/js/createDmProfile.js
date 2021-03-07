// TODO: burayı komple doldur

const form = document.querySelector('form')
const profileName = document.querySelector('#profile-name')
const messageArea = document.querySelector('.message-area')
const addButton = document.querySelector('#add-new-dm')


addButton.addEventListener('click', async e => {
    const textArea = document.createElement("textarea")
    textArea.classList.add("field-long")
    textArea.classList.add("field-textarea")
    textArea.classList.add("message")

    messageArea.appendChild(textArea)
})

form.addEventListener('submit', async e => {
    e.preventDefault()

    let messages = document.querySelectorAll(".message")
    const messageValues = []
    messages.forEach(message => messageValues.push(message.value))

    const data = {
        profileName: profileName.value,
        messages: messageValues
    }

    await fetch(`/createDmProfile`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
})