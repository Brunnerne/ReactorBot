# Reactor

Reactor is a simple Discord bot that can react to messages in a server.

This provides a simple way of initializing reaction options (e.g. for votes / planning) by a "non-user",
thus giving all real users the possibility to react selectively.

## Usage

Add reactions to a message with
```
+react <#channel> <messageID> <emoji>...
```

> **Note:** Reactor can only react with emojis from the server or emojis already used on the message


Remove any added reactions from a message again with
```
+unreact <#channel> <messageID> <emoji>...
```

## Setup

To add this bot to your own server:

- Setup a new application and bot on https://discord.com/developers/applications/
- Generate an OAUTH2 URL with scope `bot` and at least the permissions
  * `Read Messages/View Channels`
  * `Read Message History`
  * `Send Messages`
  * `Add Reactions`
- Add the bot to your server with the generated URL
- Clone this project (or just download `bot.py`) and create a `.env` file in the same folder
- Generate your bot token on the developer portal and add `BOT_TOKEN=<TOKEN>` to `.env`
- Install project dependencies with
  ```
  pip3 install discord.py python-dotenv
  ```
- Run `bot.py` to run the bot
