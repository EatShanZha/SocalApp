$(document).ready(function(){
    var content = document.getElementById("content")
    var portrait = document.getElementById("portrait")
    var inputfile = document.getElementById("inputfile")
    function showPreview() {
      var file = source.files[0];
      if(window.FileReader) {
          var fr = new FileReader();
          console.log(fr);
          fr.onloadend = function(e) {
            portrait.src = e.target.result;
          };
          fr.readAsDataURL(file);
          portrait.style.display = 'block';
      }
    }
})