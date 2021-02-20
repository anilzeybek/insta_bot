console.log('Client side js file loaded')

const processForm = document.querySelector('form')
const username = document.querySelector('#username')
const password = document.querySelector('#password')
const findHashtag = document.querySelector('#findHashtag')
const hashtagsLi = document.querySelector('#hashtagsLi')
const hashtags = document.querySelector('#hashtags')
const requestLimit = document.querySelector('#requestLimit')
const likeLimit = document.querySelector('#likeLimit')
const dmLimit = document.querySelector("#dmLimit")
const targets = document.querySelector('#targets')
const lookFollowers = document.querySelector('#lookFollowers')
const howManyFollowers = document.querySelector("#howManyFollowers")
const keywords = document.querySelector('#keywords')
const minTime = document.querySelector('#minTime')
const maxTime = document.querySelector('#maxTime')
const messageArea = document.querySelector(".message-area")

dmLimit.addEventListener('keyup', async e => {
    e.preventDefault()

    let messages = document.querySelectorAll(".messages")
    if (messages.length < parseInt(dmLimit.value)) {
        for (let i = 0; i < parseInt(dmLimit.value) - messages.length; i++) {
            const textArea = document.createElement("textarea")
            textArea.classList.add("field-long")
            textArea.classList.add("field-textarea")
            textArea.classList.add("messages")

            messageArea.appendChild(textArea)
        }
    }
})

lookFollowers.addEventListener('change', async e => {
    if (lookFollowers.checked) {
        keywords.style.visibility = "hidden";
        howManyFollowers.style.visibility = "visible"
    }
    else {
        keywords.style.visibility = "visible";
        howManyFollowers.style.visibility = "hidden"
    }
})

findHashtag.addEventListener('change', async e => {
    if (findHashtag.checked) {
        hashtagsLi.style.visibility = "visible"
    }
    else {
        hashtagsLi.style.visibility = "hidden"
    }
})

processForm.addEventListener('submit', async e => {
    e.preventDefault()
    if (findHashtag.checked) {
        if (!hashtags.value)
            alert("Hashtagleri girin")

        const data = {
            username: username.value,
            password: password.value,
            FIND_HASHTAG: findHashtag.checked,
            hashtags: hashtags.value
        }

        await fetch(`/process`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        
    } else {
        let messages = document.querySelectorAll(".messages")
        if (!username.value || !password.value || !requestLimit.value || !likeLimit.value || !dmLimit.value || !targets.value || (!keywords.value && !lookFollowers.checked)|| !minTime.value || !maxTime.value) {
            alert("Bütün alanları doldurun")
            return
        }
    
        const messageValues = []
        messages.forEach(message => messageValues.push(message.value))
    
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
            lookFollowers: lookFollowers.checked,
            howManyFollowers: parseInt(howManyFollowers.value) || 10,
            messages: messageValues
        }

        await fetch(`/process`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
    }

    window.location.href = '/'
})