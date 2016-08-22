// If you're using require(),
// this can be it's own module.
module.exports = function(dateObj) {

  var month, day, year, format_date;

  dateObj = new Date(dateObj);
  
  monthList = ["Jan.","Feb.","March","April","May","June","July","Aug.","Sept.","Oct.","Nov.","Dec."];
  
  month = monthList[dateObj.getMonth()];
  
  day = dateObj.getDate();
  
  year = dateObj.getFullYear();
  
  format_date = month + " " + day + ", " + year;

  return format_date;
}