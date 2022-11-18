document.querySelector("#roomInput").focus();


// submit if the user presses the enter key
(document.querySelector("#nameInput").onkeyup)  = function(e) {
    if (e.keyCode === 13) {  // enter key
        document.querySelector("#roomConnect").click();
    }
};

// redirect to '/room/<roomInput>/'
document.querySelector("#roomConnect").onclick = function() {
    let roomName = document.querySelector("#roomInput").value;
    let userName = document.querySelector("#nameInput").value;

    if(!roomName || !userName) {
        alert('enter both room and user name')
        return
    }
    window.location.pathname = "chat/" + roomName + "/" + userName ;
}
