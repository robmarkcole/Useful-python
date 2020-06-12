* https://github.com/theskumar/python-dotenv
## python-dotenv
* https://github.com/theskumar/python-dotenv
* You first create a .env file, which is just a text file containing variables and comments. The Python dotenv librarly, when you call load_dotenv, detects the file, and passes the variables into your system’s environment variables, where you can pull them out with the os library. This file needs to be excluded from version control by adding the following to your .gitignore:
* Discussed in this article in context of jupyter notebooks -> http://veekaybee.github.io/2020/02/25/secrets/