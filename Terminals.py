#!/usr/bin/python
# Terminals Unix startup script

#import libs
import os
import datetime
import GetDateTime
import sys
import time
import threading


class Terminals():
  # Provides a Terminals object


  def __init__(self):
    # Init
    
    # Hang whilst system logins
    #time.sleep(5)

    # Process time and date
    self.dt_handle = GetDateTime.GetDateTime()

    terminals_thread = threading.Thread(target=self.open_terminals, args=())
    terminals_thread.start()
    # Open the terminals

    # Open browser
    #self.open_browser()

    # Open RSS
    self.rss_feeds()

    # Output
    self.output_welcome_message()

    # xchat
    xchat_thread = threading.Thread(target=self.xchat, args=())
    xchat_thread.start()
    

  def output_welcome_message(self):
    # Function to output the scripts welcome message
   
    self.hash_print(20) 
    time.sleep(1)
    print("Good %s Sir" % self.dt_handle.day_part)
    print(self.dt_handle.date_string)
    print(self.dt_handle.time_string)
    time.sleep(1)

    self.hash_print(20) 

  def open_terminals(self):
    # Function to open the necessary terminals
  
    for x in range(2):
      os.system("gnome-terminal")

  def hash_print(self, quantity):
    # Function to print hashes

    for x in range(quantity):
      sys.stdout.write("#")
      sys.stdout.flush()
      time.sleep(0.1)
    sys.stdout.write("\n")

    
  def open_browser(self):
    # Function to open the browser. TODO: upgrade this to use Python's webbrowser library
    os.system("google-chrome www.arstechnica.co.uk")


  def rss_feeds(self):
    # Function to handle RSS feed news. Ideally this function will be converted to a class
    # To give better functionality in the future

    # Clear the screen, print hashes and echo message
    os.system("clear")
 
    os.system("gnome-terminal --window-with-profile=Unnamed -e '/usr/bin/newsbeuter'")


  def xchat(self):
    # Function to open xchat
  
    os.system("xchat")

if __name__ == "__main__":
  Terminals = Terminals()
