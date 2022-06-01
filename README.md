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
