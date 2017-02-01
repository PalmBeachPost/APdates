# Assumes you have an actual date object, not a string.
# Work for Window users.
Text mangling:
string = string.substitute("January ", "Jan. ").substitute("February ", "Feb. ").substitute("August ", "Aug. ").substitute("September ", "Sept. ").substitute("October ", "Oct. ").substitute("November ", "Nov. ").substitute("December ", "Dec. ")



def formatAPDate(date_object):     
    if date_object.month == 9:
        new_date = "Sept. " +  datetime.datetime.strftime(date_object, "%d, %Y").lstrip("0")
    elif date_object.month < 3 or date_object.month > 7:
        new_date = datetime.datetime.strftime(date_object, "%b. ") + datetime.datetime.strftime(date_object, "%d, %Y").lstrip("0")
    else:
        new_date = datetime.datetime.strftime(date_object, "%B ") + datetime.datetime.strftime(date_object, "%d, %Y").lstrip("0")
    return new_date


# An alternate version, adapting from a string. 
# Will fail on Windows because of %-d
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
