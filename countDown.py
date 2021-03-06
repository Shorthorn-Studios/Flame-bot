# Dependencies:
import json
import time

####################################################################################################
# Individual countDown Timer class
####################################################################################################
class countDown(object):
        # Define various interval units
        m = 60
        h = m * 60
        d = h * 24
        w = d * 7
        mo = w *4 #Assume 4 week months = 28 days/4 weeks
        countDownFile = 'countdown.json'
        ####################################################################################################
        # Initialise object with passed parameters (Number of Units, Units)
        # Some 'sensible' defaults added into constructor
        ####################################################################################################        
        def __init__(self, numbUnits = 1, unit = 'm',user = 'Username not set', name = 'Un-named timer',reminder = 0): 
                # We'll typecast the units just to be safe. Possibly use type hinting later on
                if numbUnits == None:
                        numbUnits = 0
                if int(numbUnits) < 0:
                        numbUnits = 0
                self.numUnits = int(numbUnits)
                self.unitType = unit
                if self.unitType == None:
                        self.unitType = 'm'
                self.name = name # Probably for future expansion
                if self.name == None:
                        self.name='Un-named timer'
                self.timerUser = user
                if self.timerUser == None:
                        self.timerUser='Username not set'
                self.reminder = int(reminder)
                if self.reminder == None: # Catch 'None/Null' setting
                        self.reminder = 0
        ####################################################################################################
        # Getter for total number of 'clicks' (clock is floating point representation of seconds, so don't
        # need the 1,000 multiplier). Need to re-factor tests to take into account or most will fail
        ####################################################################################################        
        def getTotalTime(self):
                self.totalTicks = self.numUnits * self.numTicks() 
                return self.totalTicks
        ####################################################################################################
        # Getter for reminder status
        ####################################################################################################        
        def getReminder(self):
                return self.reminder
        
        ####################################################################################################
        # Getter and setter for timer name....not yet fully implemented
        ####################################################################################################        
        def setName(self, text):
                self.name = text

        def getName(self):
                return self.name
  
        ####################################################################################################
        # Getter and setter for username (implement as we approach prod)
        ####################################################################################################        
        def setUserName(self, text):
                self.timerUser = text
        def getUserName(self):
                return self.timerUser
       
        ####################################################################################################
        # Handle various unit types 
        ####################################################################################################                
        def numTicks(self):
                if self.unitType == 'm':
                        return int(self.m) # I'm playing safe by typecasting here
                if self.unitType == 'h':
                        return int(self.h)
                if self.unitType == 'd':
                        return int(self.d)
                if self.unitType == 'w':
                        return int(self.w)
                if self.unitType == 'mo':
                        return int(self.mo)
                return 0          
                        
        ####################################################################################################
        # Write out this instance to json - testing of dump only at present
        ####################################################################################################
        def jsonOut(self,filename='timer.txt'):
                self.timerStartTime =  int(time.time() ) # We're only needed to be accurate to the second.
                self.timerEndTime = self.timerStartTime                     
                self.timerEndTime += self.getTotalTime()
                return json.dumps(self, default=lambda o: o.__dict__, 
                          sort_keys=True, indent=4)              


####################################################################################################
# Wrapper for 'countDown' timers - could refactor this into generically named class/file
####################################################################################################
class flamebotTimers:

        ####################################################################################################
        # We need an array - so initialise it here
        ####################################################################################################        
        def __init__(self):
                self.timers = [] 
                               
        ####################################################################################################
        # Simple method to show how many timers
        ####################################################################################################        
        def numTimers(self):
               return len(self.timers)
        
        ####################################################################################################
        # Push timer onto 'stack'
        ####################################################################################################        
        def addTimer(self,timer):
                self.timers.append(timer)
                return self
        
        ####################################################################################################
        # Check to see if any timers need to be triggered
        ####################################################################################################
        def poll(self):
                return # we don't actually want to return anything just handle the polling here