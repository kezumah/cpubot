# Raspberrypi CPU Temperature Monitor Bot

4/26/2021

##  MAIN PROGRAM SECTION 

Written by Tianhao Yu

### CREATING LOCAL VARIABLES:

1. Create CPUTemperature, twitter bot, and other local variables to access and store data.

2. Create ThingSpeak variables (channel ID, write key) to write data to ThingSpeak channel.

### CREATING FUNCTIONS

3. write_temp() function takes 2 parameters: CPU temperature and write channel. It will write the temperature to the
   ThingSpeak channel and print temperature and date and time locally. If it fails, it will print "Connection Failed"
   message and retry next time.

4. log_temp() function takes 1 parameter twitter bot. It will be executed every 10 minutes by schedule. It will take
   the time and the temperature at that time, and call write_temp() function to log the temperature to ThingSpeak. If
   the temperature recorded go above 60 degrees Celsius, it will also send a warning messages to Twitter through twitter
   bot and record the time and temperature at a local warning dictionary.

5. daily_brief() function takes 2 parameters warning dictionary and twitter bot. It will be executed at 23:50:00 by
   schedule. It will send the daily warning summary both to twitter and locally. If it has more than one warning, it
   will report the min and max temperature. Otherwise, it will report 0 warnings.

6. good_bye() function takes no parameter and it will be executed at 23:51:00 by schedule. It will print a local message
   signaling the termination of the program.

### RUNNING MAIN PROGRAM

7. Main function will print a message signaling the start of the program. Then start the schedule pending and sleeps
   every second.

7.1 Schedules are used to let a certain function run at a specific time. 3 schedule commands are used to measure CPU
temperature every 10 minutes, report daily summary at 23:50 and close the program at 23:51.

## Twitter Bot Section
#### Written by Kennedy C. Ezumah

### SETTING UP A TWITTER DEVELOPER ACCOUNT:

1. First create a Twitter Developer account and a custom Twitter App to gain access to the Twitter API.

      https://developer.twitter.com/en

2. If the Twitter account that you used to create the developer account is different from that which you will use as a bot,
   you will need to run the "authorize_nonprimary.py" module to authorize its interaction with your Twitter App (Wait until step 4 to do this).

### SETTING UP TWITTER CREDENTIALS:

3. Create a .JSON file named "twitter_api_credentials", where you will proceed to make a dictionary to store the API key and token from your Twitter App.
   Keep this file in the same working directory as your files, as this is where you will store the access key and token that you will extract from your
   bot account. It is essential to keep this information in a separate file, and avoid hard-coding it into your program in order to minimize security risks
   and make your program flexible and easy to manage.

4. Run the "authorize_nonprimary.py" file to begin the authorization process. A url will be produced. Copy the url and paste it into a separate browser.
   It is important to run this in a browser on which you are not currently signed on to your Twitter Developer account. The link will prompt you to sign in to your
   intended bot account. Sign in, authorize, and copy the pin sequence shown on the screen.

5. Paste the pin sequence into the input field on-display in python, making sure to add quotation marks to identify it as a string object:

      PIN: "AHD72O19"

6. Once this is complete, the access key and token for your bot account will be displayed. You do not have to do anything, as by this point, they have been automatically
   saved as key-value pairs in your "twitter_api_credentials" .JSON file. At this point your Twitter App has been authorized to perform actions on your
   bot account and you are ready to post!

### PUBLISHING A BOT-TWEET:

7. Run the "driver_file.py" file and enter a custom tweet. Head over to twitter to see that your tweet is successful!

## :::::::::::::::::::::::::::::::::::::::: WEB-SCRAPER SECTION :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Written by Xiaoman Yang

### CREATING FUNCTIONS

1. The get_url() function takes one parameter which will be the location of your chosen, and returns the url of that location.

2. The get_info() function takes one parameter as well, and it finds all the data you're looking for as they have different attributes under the tag,
   which includes the location of the work, the company that is hiring and a short description of what is expected for the job.
   It stores the information in a 3-element tuple and returns it.

### THE MAIN() FUNCTION

1. Create a list of locations to run through.

2. For each city, create an empty list to save the data you fetch.
   2.1. Call the get_url function to get the url
   2.2. We now have multiple pages of the searching results and we need a while loop to go through all of them
   a) For each page, send a request and retrieve the HTML.
   (But if you do it too quick/too often, the server will turn down your requests and you get nothing. That's why the time.sleep() was used a lot.)
   b) Parse the HTML code, which will return an iterable Python object.
   c) Loop through the iterable, and call the get_info() function. In this way the information we want is saved.
   2.3. Check if we hit the last page or not by finding the "Next" button. If it's the last page, move to the next town;
   if not, continue to the next page of the searching result.

3. This program will terminate when we have looped through the entire location list, or it can be interrupted manually after we have run for two hours.

### NB

1. For legal precautions, the data we get in the process will not be saved and used in any way.

2. Apart from the above concerns, the idea was to ask the pi to do different tasks for some time period, so it did not necessarily need to save the data.

3. The time.sleep() was used to keep the program running without failures, but as the execution was suspended often, it was likely to affect our project results.
   That's probably one of the reasons that the CPU temperature did not go up to 60 degrees a lot when dealing with web-scraping.

4. We have tested many times to make sure the crawler would run without any problems, it will be all good.
   But just in case if you get an empty list back (and again that's because your request is rejected by the server and you fail to get a <response [200]> ),
   wait for some extra time or change your IP address, and restart the program all over again. That should solve the problem.
