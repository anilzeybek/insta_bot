const form = document.querySelector('form')
const newPassword1 = document.querySelector('#newPassword1')
const newPassword2 = document.querySelector('#newPassword2')

form.addEventListener('submit', async e => {
    e.preventDefault()

    if (!newPassword1.value || !newPassword2.value) {
        alert("Tüm alanları doldurun")
        return
    }
    if (newPassword1.value !== newPassword2.value) {
        alert("Şifreler aynı değil")
        return
    }

    await fetch(`/settings`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({newPassword: newPassword2.value})
    })

    window.location.href = '/'
})