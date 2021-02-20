document.querySelectorAll('button').forEach(item => {
    item.addEventListener('click', async function() {
        await fetch(`/clean`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({username: this.id})
        })

        const correspondingDiv = this.parentElement;
        correspondingDiv.remove()
    })
})
  