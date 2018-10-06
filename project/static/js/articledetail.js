function review(){
    var reviewArticle = document.getElementById("reviewArticle")
    reviewArticle.style.display = "block"
    reviewArticle.focus()
    reviewArticle.addEventListener("blur", function(){
    reviewArticle.style.display = "none"
},false)
}

function review_parent(obj){
    var review_parent = document.getElementById("reviewParent")
    review_parent.placeholder = "回复:" +String(obj.id)
    review_parent.pk = obj.value
    review_parent.style.display = "block"
    review_parent.focus()
    review_parent.addEventListener("blur", function(){
    review_parent.style.display = "none"
},false)
}

function CheckInfo() {
    if (event.keyCode == 13) {
        var comment = $("#reviewArticle").val();
        var relate = document.getElementById("relate")

        $.post(window.location.pathname,{"comment":comment}, function(data){
            if (data.status == "error"){
            alert("好像有点问题啊,小老弟")
            }
            else{parent.location.reload();}
        })
        $("#reviewArticle").val('')
    }
}

function CheckInfo_Parent(obj) {
    if (event.keyCode == 13) {
        var comment = $("#reviewParent").val();
        var parent_comment = obj.pk
        var data
//        .ajax({
//            url:window.location.pathname,
//            type:'post',
//            data:{'applicants':JSON.stringify(data)},
//            async:false,
//            success:function (data){
//                alert("好像有点问题啊,小老弟")
//            }
//        })
        $.post(window.location.pathname,{"comment":comment,"parent_comment":parent_comment}, function(data){
            if (data.status == "error"){
            alert("好像有点问题啊,小老弟")
            }
            else{parent.location.reload();}
        })
        $("#reviewArticle").val('')
    }
}
$(document).ready(function(){
//    数楼层
    var floor = document.getElementsByClassName("floor")
    var k;
    for(k=0;k<floor.length;k++){
        floor[k].innerHTML = String(k+1) + "楼"
    }
//    是否加载图片
    var x = document.getElementsByClassName("list-img");
    var i;
    for(i=0;i<x.length;i++){
    if (x[i].src.length < 30){
        x[i].style.display = "none"
        }
     }
})