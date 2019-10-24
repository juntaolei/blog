import sqlite3   #enable control of an sqlite database
import csv 


  command = "CREATE TABLE users (Id INTEGER PRIMARY KEY, username TEXT);"
  c.execute(command)
    commands = list()

    newCommand = "INSERT INTO courses VALUES ('{}', {}, {});".format(row['code'], row['mark'], row['id'])
        #print(newCommand)
        commands.append(newCommand) #add all commands to a list
    for item in commands: #run each command
        c.execute(item)
