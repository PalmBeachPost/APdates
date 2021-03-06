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