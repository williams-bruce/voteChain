let userInput = "";

function handleInputChange(digit) {  
    if (userInput.length < 5) {
        userInput += digit;
        document.getElementById("userInput").value= userInput;
    }
    if (userInput.length === 5) {
        document.getElementById("voteForm").onsubmit = function () {
            return false;
        };
    }
}

function handleInputCorrection() {
    userInput = userInput.slice(0, -1);
    document.getElementById("userInput").value= userInput;
}


function handleConfirmButton() {
    document.getElementById("voteForm").onsubmit = function () {
        return true;
    }
}