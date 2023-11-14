

const auth_form = document.querySelector('[class="auth_form"]');
const message_block = document.querySelector('[class="message"]');
const login_url = '/auth/login'

auth_form.addEventListener('submit', send_auth_form);

async function send_auth_form(e) {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    data = {}
    data["email"] = email
    data["password"] = password

    let response = await fetch(login_url, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
        })

    if (response.ok) {
      let json = await response.json()
      console.log(json)
      message_block.innerHTML = '<div id="result-message" class="text-success" style="margin-top: 20px;">succes</div>';
    } else {
      console.log(await response.text())
      message_block.innerHTML = '<div id="result-message" class="text-success" style="margin-top: 20px;">error</div>';
    }



    auth_form.style.display = 'none';
}
