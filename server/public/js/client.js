console.log('Client side js file loaded')

const processForm = document.querySelector('form')
const username = document.querySelector('#username')
const password = document.querySelector('#password')
const requestLimit = document.querySelector('#requestLimit')
const likeLimit = document.querySelector('#likeLimit')
const dmLimit = document.querySelector("#dmLimit")
const targets = document.querySelector('#targets')
const keywords = document.querySelector('#keywords')
const messages = document.querySelector('#messages')
const minTime = document.querySelector('#minTime')
const maxTime = document.querySelector('#maxTime')


processForm.addEventListener('submit', async e => {
    e.preventDefault()

    if (!username.value || !password.value || !requestLimit.value || !likeLimit.value || !dmLimit.value || !targets.value || !keywords.value || !messages.value || !minTime.value || !maxTime.value) {
        alert("Bütün alanları doldurun")
        return
    }

    if (parseInt(dmLimit.value) !== messages.value.split('\n').length) {
        alert("Limit sayısı ile mesaj sayısı aynı olmalı")
        return
    }

    const data = {
        username: username.value,
        password: password.value,
        requestLimit: parseInt(requestLimit.value),
        likeLimit: parseInt(likeLimit.value),
        dmLimit: parseInt(dmLimit.value),
        minTime: parseInt(minTime.value),
        maxTime: parseInt(maxTime.value),
        targets: targets.value,
        keywords: keywords.value,
        messages: messages.value
    }

    await fetch(`/process`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })

    window.location.href = '/'
})