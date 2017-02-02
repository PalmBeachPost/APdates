# Assumes you have an actual date object, not a string.
# Work for Window users.
def ap_string(text):
    replacementpairs = [
        ("January 0", "Jan. "), ("February 0", "Feb. "), ("August 0", "Aug. "), ("September 0", "Sept. "), ("October 0", "Oct. "), ("November 0", "Nov. "), ("December 0", "Dec. "),
        ("March 0", "March "), ("April 0", "April "), ("May 0", "May "), ("June 0", "June "), ("July 0", "July "),
        ("January ", "Jan. "), ("February ", "Feb. "), ("August ", "Aug. "), ("September ", "Sept. "), ("October ", "Oct. "), ("November ", "Nov. "), ("December ", "Dec. ")
    ]
    for pair in replacementpairs:
        source, destination = pair
        text = text.replace(source, destination)
    return(text)


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
