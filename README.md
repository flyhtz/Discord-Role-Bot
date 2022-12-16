# Discord-Role-Bot

A discord bot allowing u to give custom roles to people on your server!

It works by sending a message in a channel u choose and adds reactions to that message.

When it detects someone click the reply it will give them the role connected to that reply.

# Usage 

How to use the role bot:

Open cmd in directory of "Role-Bot.py"

Make sure u have discord.py installed by doing

```bash

sudo pip install discord.py

```

**Change the Bot-Token in YOUR_BOT_TOKEN_HERE [Discord developer portal](https://discord.com/developers/applications)**

Make sure to also change the emoji's and Role names in Role-Bot.py

When you are ready run:

```bash

sudo python Role-Bot.py

```

Than go into discord and run !create_roles (you only need to do that one time)

Than go to the channel where u want the bot to send the message and send !ask_roles (u might need to re-do this if u restart the bot)