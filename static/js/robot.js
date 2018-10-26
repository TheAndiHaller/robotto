function cambiarPantalla(){
    document.getElementById("ojos").setAttribute("hidden","true");
    document.getElementById("fondo").removeAttribute("hidden","true");   
}

function botonAbrir() {
  document.getElementById("fondo").setAttribute("hidden","true");
  document.getElementById("cerrar").removeAttribute("hidden","true");
}

function botonCerrar() {
  document.getElementById("cerrar").setAttribute("hidden","true");
  document.getElementById("mas").removeAttribute("hidden","true");
}

function botonNo() {
  document.getElementById("mas").setAttribute("hidden","true");
  document.getElementById("ojos").removeAttribute("hidden","true");
}

function botonSi() {
  document.getElementById("mas").setAttribute("hidden","true");
  document.getElementById("fondo").removeAttribute("hidden","true");
}




$(function(){
    var isTouchDevice = "ontouchstart" in document.documentElement ? true : false;
    var BUTTON_DOWN   = isTouchDevice ? "touchstart" : "mousedown";
    var BUTTON_UP     = isTouchDevice ? "touchend"   : "mouseup";
                
    $("button").bind(BUTTON_DOWN,function(){
            $.post("/control",
            {boton: this.id},
            function(data,status){
              });
            });
    

    });
    
    function reqSensorData() {
      setInterval(function(){ 
        $.post("/control",
        {boton: 't'},
        function(data,status){
          //console.log("Data: " + data + "\nStatus: " + status);

          var tempindex = data.indexOf("temp:");
          var humindex = data.indexOf("hum:");
          var endindex = data.indexOf("\\r\\n");
          var temp = data.substring(tempindex + 5, humindex - 1);
          var hume = data.substring(humindex + 4, endindex);

          document.getElementById("temp").innerHTML= "Temperatura: " + temp + " Humedad: " + hume;
          });
      
      }, 5000);
  }
