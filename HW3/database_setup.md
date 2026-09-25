## 1. Add Port
As with the webserver setup, we need to add a new custom tcp connection 
to be able to host the database on port 6002. Once we've done this we 
can ssh into the instance.

## 2. Install Maria DB
This is done with `sudo apt update` and 
`sudo apt install mariadb-server -y`

## 3. Start Maria DB
Use `sudo systemctl enable mariadb` to start the database. We can also 
run `sudo mariadb-secure-installation` to add security by removing 
anonymous users.

## 4. Configure Maria DB
We want to edit the config file to set it to host on port 6002. We also 
want to bind the address to 0.0.0.0 to allow connections. Then we 
restart the database so that the changes can take effect with `sudo 
systemctl restart mariadb`

## 5. Create DB
Use `sudo maria` to log into mariadb and then we can run 
`CREATE DATABASE comp370_test` to actually create this test database

## 6. Create User
Now we want to create the comp370 user with a password which is done 
with `CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s';`, then 
`GRANT ALL PRIVELEGES ON comp370_text.* TO 'comp370'@'%';`, and finally
`FLUSH PRIVILEGES`. The % means we can connect from any IP address.

## 7. Download DBeaver
Go to the internet and download it like any other app. Then we can 
start the app.

## 8. Connect to MariaDB through DBeaver
Add a new connection and input all the information. If the database has 
a green icon, this means the connection is valid. Additionally, we can 
also test this connection by clicking the comp370_test database and 
selecting new SQL script. We can run `SELECT 1;` and if it returns 1 then 
the connection works!
