# Discord self reacting selfbot

The title is self explanatory.This bot uses the selfcord.py library.
> ⚠️ **Disclaimer**
> This project is for educational and proof-of-concept purposes only.  
> Use it at your own risk. The author assumes no responsibility for any misuse or damages.

## Installation
```bash
git clone https://github.com/MuTe43/Discord-SelfReactBot.git
cd Discord-SelfReactBot
pip install -r requirements.txt
```

## How to use
in **app.py** add your emojis in this list:
```python
emoji = ['\U0001F62D',':thonk:961423622147309618',':patrickNotes:1202293366465757315']
```
- it is adviced that you put the default emojis in Unicode format like '\U0001F62D' for a sob.
- if you want to use a custom server emoji (like the 2nd and 3rd element of the array) you have to go to a specific server type \  in the message box then select the emoji you want it should display a pair like the ones in the list above.

in **.env**
you put your discord account's token
`ACCOUNT_TOKEN= "here"`

after everything is done, you run the python script
```bash
cd Discord-SelfReactBot # if you're not in the directory
./app.py
```