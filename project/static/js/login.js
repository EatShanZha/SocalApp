$(document).ready(function(){
    var account = document.getElementById("account")
    var accountcheck = document.getElementById("accountcheck")
//    account.addEventListener("focus", function(){
//        accountcheck.style.display = "none"
//    },false)
    account.addEventListener("blur", function(){
        instr = this.value
        $.post("/checkuserid/", {"userid":instr}, function(data){
            if (data.status == "success"){
                accountcheck.style.display = "block"
            }
        })
    },false)

})