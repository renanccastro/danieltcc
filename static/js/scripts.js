/*!
* Start Bootstrap - Blog Home v5.0.8 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
function sendReq() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("req").innerHTML = this.responseText;
     var acessaDados=JSON.parse(this.responseText)
      console.log( acessaDados.cifrado)
      }
    };
    xhttp.open("GET", "https://enderecodaapidobackend", true);
    xhttp.send();
  
  }
  
  function produto(array) {
  
    var produtoDoArray = 1;
  
    for (var i = 0; i < array.lenght; i++) {
      produtoDoArray = produtoDoArray * array[i];
    }
    return produtoDoArray
  }
    
  