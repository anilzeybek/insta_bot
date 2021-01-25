console.log('Client side js file loaded')

const processForm = document.querySelector('form')
const username = document.querySelector('#username')
const password = document.querySelector('#password')
const requestLimit = document.querySelector('#requestLimit')
const likeLimit = document.querySelector('#likeLimit')
const targets = document.querySelector('#targets')
const keywords = document.querySelector('#keywords')

processForm.addEventListener('submit', async e => {
    e.preventDefault()

    if (!username.value || !password.value || !requestLimit.value || !likeLimit.value || !targets.value || !keywords.value) {
        alert("Bütün alanları doldurun")
        return
    }

    const data = {
        username: username.value,
        password: password.value,
        requestLimit: parseInt(requestLimit.value),
        likeLimit: parseInt(likeLimit.value),
        targets: targets.value,
        keywords: keywords.value
    }

    const response = await fetch(`/process`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })

    window.location.href = '/'
})