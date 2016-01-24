# GetDateTime library script
# Provides the date time functionality necessary for Terminals

# Lib imports
import datetime

class GetDateTime():
  # Provides a GetDateTime object

  def __init__(self):
    # Init - Perform Date Time processing 
    handle = datetime.datetime.now()

    # Create datetime dict
    self.date_dict = {
		  "hour": handle.hour,
		  "minute": handle.minute,
		  "second": handle.second,
		  "year": handle.year,
		  "month": handle.month,
		  "day": handle.day
		}

    # Pad with zeros if necessary
    for item in self.date_dict.iteritems():
      if int(item[1]) < 10:
	self.date_dict[item[0]] = "0" + str(item[1])

    # Create Date and Time strings
    self.date_string = "Date: %s-%s-%s" % (self.date_dict["day"], self.date_dict["month"], self.date_dict["year"]) 
    self.time_string = "Time: %s:%s:%s" %( self.date_dict["hour"], self.date_dict["minute"], self.date_dict["second"])


    # Set day part
    if int(self.date_dict["hour"]) >= 12:
      self.day_part = "Afternoon"
    else:
      self.day_part = "Morning"
