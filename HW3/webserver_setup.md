# Setting Up a Webserver

1. First we want to make sure the server is configured for a custom tcp 
   connection on port 8008. This can be done in the security tab inside 
   AWS. You might want to stop and restart the instance to make sure 
   this works correctly.

2. Now you want to install apache. This can be done using `sudo apt 
update`, and `sudo apt install apache2 -y`

3. Then we want to make sure apache is listening on the right port. To 
   do this we do `sudo nano /etc/apache2/ports.conf`, and add `Listen 8008`

4. Next we want to do a similar thing to set the default port to 8008 
   by doing: `sudo nano /etc/apache2/sites-available/000-default.conf`

5. Now that we've made these changes so that the webserver is on the 
   right port, we want to restart apache like so: `sudo systemctl 
   restart apache2`

6. Now we need to get the actual file. We can do this by creating a new 
   file with vim, or using wget to get the file that we've already made 
   and put in our github repo.

7. Now we want to copy the file into the apache root. This is done with 
   the `cp` command. More precisely, we want to copy the file into 
`/var/www/html/`

8. At this point we can check our browser and verify that the file is 
   there: http://PUBLIC_IP:8008/comp370_hw3.txt, where PUBLIC_IP is the 
   public IP listed in AWS and the one we used to ssh into the instance.