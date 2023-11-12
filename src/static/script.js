let studentId = "";
let candidateId = "";
let pageState = "entry";

function handleInputChange(digit) {
    if (pageState == "entry") {
        if (studentId.length < 5) {
            studentId += digit;
            document.getElementById("userInput").value= studentId;
        }
    }
    else if (pageState == "voteSection") {
        if (candidateId.length < 5) {
            candidateId += digit;
            document.getElementById("userInputCandidate").innerHTML= candidateId;
        }
    }
}

function handleInputCorrection() {
    if (pageState == "entry") {
        studentId = studentId.slice(0, -1);
        document.getElementById("userInput").value= studentId;
    }
    else if (pageState == "voteSection") {
        candidateId = candidateId.slice(0, -1);
        document.getElementById("userInputCandidate").innerHTML= candidateId;
    }
}

function closeStudentNotFoundPage() {
    document.getElementsByClassName("initialScreen")[0].style.display = "block";
    document.getElementsByClassName("studentNotFound")[0].style.display = "none";
    studentId = "";
    document.getElementById("userInput").innerHTML= studentId;
}

function handleConfirmButton() {
    if (pageState == "entry") {
        if (codesList.indexOf(studentId) == -1) {
            document.getElementsByClassName("initialScreen")[0].style.display = "none";
            document.getElementsByClassName("studentNotFound")[0].style.display = "block";
            setTimeout(closeStudentNotFoundPage, 1500);
        }
        else {
            document.getElementsByClassName("initialScreen")[0].style.display = "none";
            document.getElementsByClassName("studentFound")[0].style.display = "block";
            document.getElementById("studendFoundMessage").innerHTML = `VOTAÇÃO PRONTA PARA ${namesList[codesList.indexOf(studentId)]}`;
            setTimeout(closeStudentFoundPage, 2000);
        }
    }
    else if (pageState == "voteSection" && candidatesCodesList.indexOf(candidateId) !== -1) {
        document.getElementsByClassName("votePage")[0].style.display = "none";
        document.getElementsByClassName("endPage")[0].style.display = "block";
        setTimeout(closeEndPage, 3000);
    }
}

function handleNULLButton() {
    if (pageState == "voteSection") {
        document.getElementsByClassName("votePage")[0].style.display = "none";
        document.getElementsByClassName("endPage")[0].style.display = "block";
        setTimeout(closeEndPage, 3000);
    }
}