/* Just testing ------*/
class Student {
    constructor (name, code) {
        this.name = name;
        this.code = code;
    }
}

class Candidate {
    constructor (name, code) {
        this.name = name;
        this.code = code;
    }
}

let student_1 = new Student("HAMILTON", "21409");
let student_2 = new Student("BRUCE", "21109");
let student_3 = new Student("LEO", "21030");

let cadidate_1 = new Candidate("IVO LIN", "21037");
let cadidate_2 = new Candidate("GANDOLFI", "21009");
let cadidate_3 = new Candidate("ASFORA", "21022");

let codesList = [student_1.code, student_2.code, student_3.code];
let namesList = [student_1.name, student_2.name, student_3.name];


let candidatesCodesList = [cadidate_1.code, cadidate_2.code, cadidate_3.code];
let candidatesNamesList = [cadidate_1.name, cadidate_2.name, cadidate_3.name];

/*--------------------*/

let studentId = "";
let candidateId = "";
let pageState = "entry";

function handleInputChange(digit) {
    if (pageState == "entry") {
        if (studentId.length < 5) {
            studentId += digit;
            document.getElementById("userInput").innerHTML= studentId;
        }
    }
    else if (pageState == "voteSection") {
        if (candidateId.length < 5) {
            candidateId += digit;
            document.getElementById("userInputCandidate").innerHTML= candidateId;
        }
        if (candidatesCodesList.indexOf(candidateId) == -1) {
            document.getElementById("candidateName").innerHTML = "NÃO ENCONTRADO";
        }
        if (candidatesCodesList.indexOf(candidateId) !== -1) {
            document.getElementById("candidateName").innerHTML = candidatesNamesList[candidatesCodesList.indexOf(candidateId)];
            document.getElementById("candidateImageElement").src = `assets/images/${candidateId}.png`
        }
    }
}

function handleInputCorrection() {
    if (pageState == "entry") {
        studentId = studentId.slice(0, -1);
        document.getElementById("userInput").innerHTML= studentId;
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

function closeStudentFoundPage() {
    pageState = "voteSection";
    document.getElementsByClassName("studentFound")[0].style.display = "none";
    document.getElementsByClassName("votePage")[0].style.display = "block";
}

function closeEndPage() {
    pageState = "entry"
    document.getElementsByClassName("endPage")[0].style.display = "none";
    document.getElementsByClassName("initialScreen")[0].style.display = "block";
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