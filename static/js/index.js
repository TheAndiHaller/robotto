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
    
            $("button").bind(BUTTON_UP,function(){
            $.post("/control",
            {boton: "alto"},
            function(data,status){
              });
            });
    });

