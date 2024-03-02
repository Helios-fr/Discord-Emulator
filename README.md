# Discord Emulator
This project emulates discord in the terminal

## Usage
To run the emulator first download the requirements in the requirements.txt file
```shell
pip3 install -r requirements.txt
```

For the emulator to work a token is needed. To get the token of your account paste the script found [here](https://gist.githubusercontent.com/Nyx-177/75cde51fb450e1442dbabf5ed508d379/raw/f2bb5529ec81ac9cb92a22082b44bfcaab6bcc8d/Discord%2520Token.js) in the developer console of [discord](https://discord.com/app) and press enter. The token will be printed in the console.

After getting the token, create a file called `token.secret` in the root directory of the project and paste the token in the file. Or if want to have the token in an enviroment variable comment line 8 of `main.py` and uncomment line 7.

To run the emulator run the following command in the source directory.
```shell
python3 main.py
```