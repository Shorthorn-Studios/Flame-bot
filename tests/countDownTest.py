#############################################################################################################################
# Very simple test framework that will exercise various functions within our code. Will only produce output on failure.
#############################################################################################################################

# Set up directory structure - we need to do this because our source code is in the parent directory of this one.
import sys

sys.path.append("../")


# Unit under test
from countDown import countDown

# We're going to use a test-driven development methodology, so our tests should reflect what we want the program to do.

# We want to be able to assign a set number of time-period (of a given unit [m h d w mo]) after which the countdown will trigger an alarm....
units = 'm' # lets start with something simple - minutes (we can hard-code the 6000 'ticks' initially)
timer = countDown(5,units)
if timer.getTotalTime() <> 300000: # 60 * 5 * 1000 = 300000
    print(timer.getTotalTime())
    print("Failed in asserting 6000 minutes == 300000 'ticks'")

# Let's stick to minutes, so we can test for example a zero input in terms of units (should return 0 - simple multiplication)
timer = countDown(0,units)
if timer.getTotalTime() <> 0: # Anything multiplied by zero is always zero
    print("Failed in asserting zero units will always give a zero time")
  
# What about a negative value - should we raise an exception? How else should we deal? Assume -ve = zero for our purposes
timer=countDown(-5,units)
if timer.getTotalTime() <> 0: # As per above - set to zero to ignore
    print("Failed handling a negative amount of minutes")

# OK Let's try a duration of 1 hour (should be 60*60*1000 = 3600000 'ticks'
units = 'h'
timer=countDown(1,units)
if timer.getTotalTime() <> 3600000:
    print("Failed setting 'ticks' to one hour")

# Same test for days = 3600000 * 24 =  86400000
units = 'd'
timer=countDown(1,units)
if timer.getTotalTime() <> 86400000:
    print("Failed setting 'ticks' to one day")

# And weeks (7 * 86400000) = 604800000
units = 'w'
timer=countDown(1,units)
if timer.getTotalTime() <> 604800000:
    print("Failed setting 'ticks' to one week")
    
# Finally months (4 * 604800000) = 2419200000
units = 'mo'
timer=countDown(1,units)
if timer.getTotalTime() <> 2419200000:
    print("Failed setting 'ticks' to one month")

# Test for nonsensical unit string (should return 0)
units = 'z'
timer=countDown(1,units)
if timer.getTotalTime() <> 0:
    print("Failed setting units to non-existent type")
    
# Test default username in constructor
username='Freddy'
timer=countDown(1,units) 
if timer.getUserName() <> 'Username not set':
    print("Failed setting default username in constructor")
# Change username post-constructor (setter test)
timer.setUserName(username)
if timer.getUserName() <> username:
    print("Failed changing username post-constructor (setter)")
# Test setting username in constructor
timer=countDown(1,units,'Marcus')
if timer.getUserName() <> 'Marcus':
    print("Failed setting username in constructor")
# Last line to signal completion of test

# Test default timer name in constructor
timername='My Timer'
timer=countDown(1,units)
if timer.getName() <> 'Un-named timer':
    print("Failed setting default timer name")
# Test setting timer name in constructor
timer=countDown(1,units,username,timername)
if timer.getName() <> timername:
    print("Failed setting timer name in constructor")
# Test changing timer name using setter
timer.setName('Joe')
if timer.getName() <> 'Joe':
    print("Failed setting timer name in setter")

# Next test should be for excessive numbers of parameters and also no parameters passed to constructor - make sure we fail gracefully


print("All Tests completed")