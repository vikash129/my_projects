// const roomName = JSON.parse(document.getElementById('room_name').textContent);
const roomName = "publichat";
const send_btn = document.getElementById('send_btn')

let connection = false ;

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
);
document.querySelector('#messageInput').focus();



send_btn.addEventListener('click' , () => {
    if (connection){
        const message = document.getElementById('messageInput').value 
        chatSocket.send( JSON.stringify({
            'command' : 'chat_message' ,
            'message' : message  

        }))
        document.getElementById('messageInput').value = ''
        console.log(message)
    }
    else{
        console.log('connection is not establishd')
    }

})


        chatSocket.onopen = () => {
            connection  = true ;
            console.log('connected')
        }

        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);

            console.log(data)

            if (data.warning){
                document.getElementById('warning').innerHTML = "Please Login to Chat <a href = 'login/'> LogIn </a>"
            }
            else if (data.type == "chat_message") {
                    const message = `
                    <div class="message d-flex flex-column">
                    <h5 class="username text-success">${data.user}</h5>
                    <h6 class="message-chat text-secondary"> ${data.message} </h6>
                </div>
                    `
                    const chat = document.getElementsByClassName('chat')[0]
                    chat.innerHTML += message 
            }
            // document.querySelector('#chat-log').value += (data.message + '\n');
        };

        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

     