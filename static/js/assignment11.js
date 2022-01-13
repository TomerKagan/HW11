getUsers = () => {
    console.log('aaa')
    let id = document.getElementById("id").value;
    console.log(id)
    fetch('https://reqres.in/api/users/'+id).then((res) => {
        return res.json()
    }).then(data=> {
        const users = document.querySelector("users");
            const info = document.createElement('info');
            info.innerHTML = `
                <span>${data.data.first_name} ${data.data.last_name}</span>
                <br>
                <a href="mailto:${data.data.email}">Send Email - ${data.data.email}</a>
                <br><br>
            `;
            users.appendChild(info);
    }).catch(
        err => console.log(err)
    )
}