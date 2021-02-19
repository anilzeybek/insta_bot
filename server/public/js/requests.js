const form = document.querySelector('form')
const username = document.querySelector('#username')
const password = document.querySelector('#password')
const days = document.querySelector('#days')
const minTime = document.querySelector('#minTime')
const maxTime = document.querySelector('#maxTime')


form.addEventListener('submit', async e => {
    e.preventDefault()

    if (!username.value || !password.value || !days.value || !minTime.value || !maxTime.value) {
        alert("Bütün alanları doldurun")
        return
    }

    const data = {
        username: username.value,
        password: password.value,
        UNDO_REQUEST: true,
        days: parseInt(days.value),
        minTime: parseInt(minTime.value),
        maxTime: parseInt(maxTime.value)
    }

    await fetch(`/requests`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })

    window.location.href = '/'
})