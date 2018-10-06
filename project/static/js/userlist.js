$(document).ready(function(){
    var useraccount = document.getElementsByClassName("usermodel")
    useraccount.addEventListener("onclick", function(){
        useraccount = this.id
        $.get("/userdetil/", {"useraccount":useraccount}, function(data){
            if (data.status == "error"){
                accountcheck.style.display = "block"
            }
        })
    },false)
})


