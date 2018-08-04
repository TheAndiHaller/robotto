// aca empieza el codigo del preloader

var w = window.innerWidth;
if (w > 800) {
  var progress = setInterval(function () {
    var $bar = $("#bar");

    if ($bar.width() >= 600) {
      clearInterval(progress);
    } else {
      $bar.width($bar.width() + 60);
    }
    $bar.text($bar.width() / 6 + "%");
    if ($bar.width() / 6 == 100) {
      $bar.text("Still working ... " + $bar.width() / 6 + "%");
    }
  }, 800);

  $(window).on('load', function () {
    $("#bar").width(600);
    $(".loader").fadeOut(3000);
  });
} else {
  var progress = setInterval(function () {
    var $bar = $("#bar");

    if ($bar.width() >= 400) {
      clearInterval(progress);
    } else {
      $bar.width($bar.width() + 40);
    }
    $bar.text($bar.width() / 4 + "%");
    if ($bar.width() / 4 == 100) {
      $bar.text("Still working ... " + $bar.width() / 4 + "%");
    }
  }, 800);

  $(window).on('load', function () {
    $("#bar").width(400);
    $(".loader").fadeOut(3000);
  });
}

// aca empieza el codigo de los botones
$(function () {
  var isTouchDevice = "ontouchstart" in document.documentElement ? true : false;
  var BUTTON_DOWN = isTouchDevice ? "touchstart" : "mousedown";
  var BUTTON_UP = isTouchDevice ? "touchend" : "mouseup";

  $("button").bind(BUTTON_DOWN, function () {
    $.post("/control",
      { boton: this.id },
      function (data, status) {
      });
  });

  $("button").bind(BUTTON_UP, function () {
    $.post("/control",
      { boton: "alto" },
      function (data, status) {
      });
  });
});
