const form = document.querySelector('form')
const username = document.querySelector('#username')
const password = document.querySelector('#password')
const hashtags = document.querySelector('#hashtags')

form.addEventListener('submit', async e => {
    e.preventDefault()
    // TODO: kullanıcının girdiği değerleri kontrol et

    const data = {
        username: username.value,
        password: password.value,
        FIND_HASHTAG: true,
        hashtags: hashtags.value
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