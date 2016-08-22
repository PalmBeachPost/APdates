# AP date formatting in a bunch of languages

Find thee text file for the language you want, or scroll down.

Pull requests for fixes or especially new languages (we're looking at you, Rubyists and R-whatevers!) are most welcomed.

#### Contributors

Chris Alcantara (@chrisalcantara), Matthew Dudak (@mjdudak), Ted Han (@knowtheory), Mike Stucka (@stucka), Andrew Tran (@andrewbtran)





##### Excel

```excel
Just a date, not date and time:
=SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(TEXT(B1, "mmmm d, yyyy"), "January", "Jan."), "February", "Feb."), "August", "Aug."), "September", "Sept."), "October", "Oct."), "November", "Nov."), "December", "Dec.")

The below is looking for a date and time, but it's easy enough to change the middle part to whatever you want.
=SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(TEXT(A2, "mmmm d, yyyy") & ", at " & TEXT(A2, "h:mm am/pm"), "AM", "a.m."), "PM", "p.m."), "January", "Jan."), "February", "Feb."), "August", "Aug."), "September", "Sept."), "October", "Oct."), "November", "Nov."), "December", "Dec.")

```



##### JavaScript

```javascript
// Dates by Chris Alcantara
function formatDate (dateObj) {

  var month, day, year, format_date;

  dateObj = new Date(dateObj);
  
  monthList = ["Jan.","Feb.","March","April","May","June","July","Aug.","Sept.","Oct.","Nov.","Dec."];
  
  month = monthList[dateObj.getMonth()];
  
  day = dateObj.getDate();
  
  year = dateObj.getFullYear();
  
  format_date = month + " " + day + ", " + year;

  return format_date;
}

formatDate('1-2-1992'); // Jan. 2, 1992
formatDate('1/2/1992'); // Jan. 2, 1992
formatDate('January 2 1992'); // Jan. 2, 1992
formatDate('01/02/92'); // Jan. 2, 1992

```



##### Python

```python
def formatAPDate(date_object):     # via Chris Alcantara and Matthew Dudak, then adapted for Windows by @stucka. Assumes you have an actual date object, not a string.
    if date_object.month == 9:
        new_date = "Sept. " +  datetime.datetime.strftime(date_object, "%d, %Y").lstrip("0")
    elif date_object.month < 3 or date_object.month > 7:
        new_date = datetime.datetime.strftime(date_object, "%b. ") + datetime.datetime.strftime(date_object, "%d, %Y").lstrip("0")
    else:
        new_date = datetime.datetime.strftime(date_object, "%B ") + datetime.datetime.strftime(date_object, "%d, %Y").lstrip("0")
    return new_date



An alternate version, adapting from a string. Will fail on Windows because of %-d
Python version by Chris Alcantara and Matthew Dudak:

def formatAPDate(date):
    
    date_object = datetime.datetime.strptime(date, "%Y-%m-%d")   
    # Handles Sept.
    if date_object.month == 9:
        new_date = datetime.datetime.strftime(date_object, "Sept. %-d, %Y")
        return new_date
    
    elif date_object.month < 3 or date_object.month > 7:
        new_date = datetime.datetime.strftime(date_object, "%b. %-d, %Y")
        return new_date
        
    else:
        new_date = datetime.datetime.strftime(date_object, "%B %-d, %Y") 
return new_date

```



##### R

```r
# this uses the R library Lubridate
# if you don't have that installed, uncomment and run the line below
# install.packages("lubridate")

library(lubridate)

# formats month-day-year format
# October 1, 1980 or 10-1-1980 or 10/1/1980, etc
# example - format_mdy("10/1/1980")

format_mdy <- function(x) {
  x <- mdy(x)
  month <- month(x, label=T, abbr=T)
  day <- day(x)
  year <- year(x)
  paste0(month, ". ", day, ", ", year)
}
  
# formats day-month-year format
# 1 Oct, 1980 or 1-10-1980 or 1-10-1980, etc 
# example - format_dmy("1 Oct, 1980")

format_dmy <- function(x) {
  x <- dmy(x)
  month <- month(x, label=T, abbr=T)
  day <- day(x)
  year <- year(x)
  paste0(month, ". ", day, ", ", year)
}

# formats year-month-day format
# 1980-10-1 or 1980-10-1, etc 
# example - format_ymd("1980-10-1")

format_ymd <- function(x) {
  x <- ymd(x)
  month <- month(x, label=T, abbr=T)
  day <- day(x)
  year <- year(x)
  paste0(month, ". ", day, ", ", year)
}
```



##### SQL

```sql
replace(replace(replace(replace(replace(replace(replace(date_format(mydate, "%M %e, %Y"), "January", "Jan."), "February", "Feb."), "August", "Aug."), "September", "Sept."), "October", "Oct."), "November", "Nov."), "December", "Dec.")

```


