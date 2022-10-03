# pfp ~ Python for Physics

## Initial setup

- Install git for windows, python, vscode (and if feeling pro, WSL and Debian)

- run VScode, click on Extensions and install "Dev Containers"

- In cmd (Windows + R then type cmd and hit enter)

- Test and Set up git (expect no errors with these - google the errors if you get any)\
`git --version`
`git config --global user.name "your name"`
`git config --global user.email "your@email.add"`
- Set up ssh - accept all the prompts and don't put in a password - vscode does not like it (one weakness of it)\
`ssh-keygen`
- Send me the full contents of the file .ssh\id_rsa.pub (you can get this in cmd with:\
`type c:\Users\<your user name>\.ssh\id_rsa.pub`
- If you are like me, then ssh will not quite work yet - [you need to follow the instructions here](https://stackoverflow.com/questions/15589682/ssh-connect-to-host-github-com-port-22-connection-timed-out) to make a file config in your .ssh folder (not needed in WSL Debian!!)
- Test ssh (this should not time out - if it does make sure you have done the above!)
`ssh -T git@github.com`

## Now we will set up a project:

- make sure python is working - if this command does not work take to google - I found typing just "python" in to cmd took me to the Windows store and I installed it there:\
`python --version`
- make a folder for all your projects:\
`mkdir projects`
- Get in to that folder:\
`cd projects`
- Grab the project from github (this will only work if you have sent me your ssh .pub key. This will make a new folder pfp with the project in\
`git clone git@github.com:mrwp-physics/pfp.git`
- Go in to the project folder\
`cd pfp`
- Make a venv in folder .venv\
`python -m venv .venv`
- Activate the venv - you should see (.venv) appear at the start of every line to tell you you are in it\
`.venv\Scripts\activate`
Test the venv (they should both give a sensible output):\
`python --version`
`pip list`
- Start vscode:
`code .`
- Double-click *ball.py* in the folders on the left.
- Install required modules for the test script to run (You can do this in vscode in the console window at the bottom of the screen)
`pip install matplotlib`
- In VSCode - on the left, Run > Run and Debug > Current window and hopefully you will have a running script. You can edit it as you like - if you get this far contact me and I will talk you through making your own copy of the script to play with.
-When you are done, you can kill the venv thusly:\
`deactivate`
