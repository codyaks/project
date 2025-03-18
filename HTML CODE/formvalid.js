function validate(e){
    e.preventDefault();
var email=document.getElementById("email").value;
var pass=document.getElementById("pass").value;
var age=document.getElementById("age").value;
var msgbox=document.getElementById("message");
let msg="";
alert("validate the form");
if (email==""){
    msg="Please enter a valid Email Id";
    msgbox.style.color="red";
}
else if (pass==""){
    msg="please enter a 8 character password";
    msgbox.style.color="red";
}
else if (age==""){
    msg="age must be between 18 to 45";
    msgbox.style.color="red";
}
else{
    msg="login successful";
    msgbox.style.color="green";
}
msgbox.innerText=msg;

}