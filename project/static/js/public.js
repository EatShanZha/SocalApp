$(document).ready(function(){

    var x = document.getElementsByClassName("list-img");
    var i;
    for(i=0;i<x.length;i++){
    if (x[i].src.length < 30){
        x[i].style.display = "none"
        }
     }
})
var article_id = document.getElementsByClassName("po-cmt")
    var k;
    for(k=0;k<article_id.length;k++){
        article_id[k].addEventListener("onclick", function(){
            article_id = this.id
            $.get("/articledetail/", {"article_id":article_id}, function(data){
                if (data.status == "error"){
                    alter("youwenti")
                }
            })
        },false)
    }

function articledetail(id){
    url = '/articledetail/'+ id
    window.location.href= url
}



