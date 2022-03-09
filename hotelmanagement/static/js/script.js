// Navbar
$(window).on('scroll'), function(){
  if ($(window).scrollTop()){
    $('nav').addClass('black');
  }
  else
  {
    $('nav').removeClass('black');
  }
}
var todayDate = new Date();
var month = todayDate.getMonth()+1; //04 - current month
var year = todayDate.getUTCFullYear(); //2021 - current year
var tdate = todayDate.getDate(); // 27 - current date 
if(month < 10){
  month = "0" + month //'0' + 4 = 04
}
if(tdate < 10){
  tdate = "0" + tdate;
}
var minDate = year + "-" + month + "-" + tdate;
document.getElementById("demo").setAttribute("min", minDate);

