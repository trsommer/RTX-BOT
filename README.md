# RTX-BOT

## Installation

1.  install python 3.x

2. install bot via console

   ```shell
   $ cd {path/to/your/basefolder} 
   $ git clone https://github.com/trsommer/RTX-BOT.git
   $ pip install -r requirements.txt (for Chrome/Chromium 89.x)
   ```



### Dependencies (manual install)

- selenium

  ```shell
  $ pip install selenium
  ```

- chromedriver_py (other versions [here](https://pypi.org/project/chromedriver-py/#history)) 

  ```shell
  $ pip install chromedriver_py==[yourversion]
  ```

- requests

  ```shell
  $ pip install requests
  ```



## Setup

1.  add cards you want to open links for (e.g. rtx3080 and rtx3080ti)

   ```python
   rtxCards = [
    #"3060",
    #"3060ti",
    #"3070",
    #"3070ti",
     "3080",
     "3080ti"
    #"3090"
   ]
   ```

2.  select the URLs you want to open

   ```python
   urls = ["www.notebooksbilliger.de", "www.ldlc.com"]
   ```

3.  set delay times (time between every check for new links) (min, max)

   ```python
   delayTimes =[0.05, 0.1]
   ```

4.  add your discord credentials

   ```python
   email = "[your discord email]"
   password =  "[your discord password]"
   ```

5.  enable notifications (follow tutorial on pushed.co)

   ```python
   enableNotifications = 0 #1 for enabled
   appKey = "[your pushed.co appKey]"
   appSecret = "[your pushed.co appSecret]"
   ```



## Usage

1.  join the stockdrops discord server
   [discord invite](https://discord.com/invite/stockdrops)

2.  start the bot from your console

   ```shell
   $ cd {path/to/your/basefolder} 
   $ python bot.py
   ```

3. let the magic happen



## Known Problems

- Sometimes discord login will not submit - press the login button manually for now
- Discord sometimes has a login captcha - fill out manually for now
