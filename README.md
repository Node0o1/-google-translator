# not-google-translator
Source code for a Discord language translator-bot using a custom api comprised of Google's public language translation tool, discord.py, and selenium web driver using the firefox browser which enables people of different ethnicities/regions the ability to communicate effectively at no cost without sharing a common language within the Discord platform.

>NOTES: It's a little slow as it needs to allow the translation to happen via browser before returning the results
>and sending the results back to the calling Discord server. The alternative would be to pay for access to Google's cloud translation api.
>
>This is not meant to be downloaded form git as an application in whole, but rather to make the source code public. Token not included. To run this bot as your own, you need to install selenium and gecko driver, decko driver needs to be added to path, and you will need to create a bot with your account at `https://discord.com/developers/applications` to recieve a valid login token. That token will need to be saved inside a .env file as `TOKEN=YOUR_TOKEN` within the same directory as the source files..
>
>NEVER SHARE YOUR LOGIN TOKENS WITH ANYONE!
