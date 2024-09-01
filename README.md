# Password-Manager
This Python program is a simple password management tool that allows users to store, update, and easily copy passwords to the clipboard. The passwords are stored using Python's "shelve" module, which allows the data to persist between sessions.

## Setup:
1.Ensure Python is installed on your system along with the necessary modules (pyperclip, shelve).
2.Place the Python script in a directory of your choice.
3.The absolute path of this folder should be added to the system path on 
  Windows so that you can run the batch files in it from the Run dialog. To 
  do this, modify the PATH environment variable.
  Say the absolute path for this folder is C:\Users\YourName\Password Manager.
  Click the Start button and type --> Edit environment variables for your account.
  From System variables, select the Path variable --> click Edit --> New --> 
  paste C:\Users\YourName\Password Manager --> Click OK.

## Working:
Press Win + R to open the Run dialog. Or you can run it by opening command prompt.
### If no argument or more than one arguments are passed , the program will show a menu with options to update or copy a password. Example:
> "py" or "py xxx xxx.."

## Updating a Password:
To update or add a password, run the script with the "update" argument:
> "py update"

## Copying a Password:
> Type "pm accountName"
If accountName exist in the file/ updated previously then it will be copied automatically to the clipboard.


### WARNING: The data stored by the program is not encripted, and can be access with any python program.
