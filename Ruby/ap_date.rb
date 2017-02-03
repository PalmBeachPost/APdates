require 'date'

# Converts the DateTime object or a valid DateTime string into AP format
#
# @param date_obj [DateTime] or [String]
# @return [String] AP format date
def format_ap_date(date_obj)
  date_obj = DateTime.parse(date_obj) unless date_obj.is_a? DateTime

  if [*3..7].include? date_obj.month # months 3,4,5,6,7 are written as is in AP
    date_obj.strftime('%B %-d, %Y')
  elsif date_obj.month == 9 # Sept. is special
    date_obj.strftime('%bt. %-d, %Y')
  else # 3 letter abbr with .
    date_obj.strftime('%b. %-d, %Y')
  end
end
