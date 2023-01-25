# Discord bug-report bot


<div align="center">
  <kbd>
    <img src="https://i.imgur.com/C7HQrV8.png" />
    <img src="https://i.imgur.com/kGWQ6UL.png" />
  </kbd>
</div>

## Description

[Discord](https://discord.com/) bot, for storing your users feedback and bug reports into [Notion](https://www.notion.so/).

### Features

- ⚙️ Easily configurable and customizable
- 🐳 All code is containerized using Docker
- 🗳️ Notion databases integration

### Built with

- [Python 3.10](https://www.python.org/)
- [Docker](https://www.docker.com/) 
- [discord.py](https://discordpy.readthedocs.io/en/stable/api.html) 
- [Notion API](https://developers.notion.com/)

## Getting started

### Prerequisites

```
Dependencies are included into docker image, we took care of it. 
```

### Install

```DOCKERFILE
docker pull psychemisss/aqua-bot-bugreports:latest
```

### Configure 
_All listed bellow parameters required for start. Configuration template file is inside the repository._

* `DISCORD_TOKEN` - Your bot token, you can get it from [here](https://discord.com/developers/applications). If you don't have an application for now, create it using this [guideline](https://discord.com/developers/docs/getting-started) 
* `DISCORD_GUILD` - Discord server ID where bot will be used. There are some instructions how to get your guild id  👇 
```
1. In Discord, open your User Settings by clicking the Settings next to your user name on the bottom.
2. Go to Appearance and enable Developer Mode under the Advanced section, then close User Settings.
3. Open your Discord server, right-click on the server name, then select Copy ID.
4. Paste it as a DISCORD_GUILD to .env, or pass it to docker container at startup.
```
* `NOTION_DATABASE` - id of a Notion list where reports info will be stored. To get it, open your database and copy id from the example below.
```
https://www.notion.so/myworkspace/a8aec43384f447ed84390e8e42c2e089?v=...
                                  |---------- Database ID -------|
```
* `NOTION_SECRET` - Token used to access your notion databases and pages, instructions of getting it are listed [here](https://www.notion.so/my-integrations).
* `NOTION_VERSION` - Specifies Notion API version and affect its functionality. If you are not sure what it does, set to `2022-02-22`


### Usage
*Running using .env to configure*
```bash
docker run --env-file ./env --name YOUR_CONTAINER_NAME psychemisss/aqua-bot-bugreports:latest
```
*Configuring env's manually*
```bash
docker run --e DISCORD_TOKEN=YOUR_TOKEN_HERE \
  DISCORD_GUILD=YOUR_GUILD_HERE \
  NOTION_DATABASE=YOUR_DATABASE \
  NOTION_SECRET=YOUR_SECRET \
  NOTION_VERSION=YOUR_VERSION \
  --name YOUR_CONTAINER_NAME psychemisss/aqua-bot-bugreports:latest
```
**After followed actions are done, and your bot came online, you can use it by typing `/feedback` and `/feedback_menu` commands inside your discord server**

### Developers Guide
For now there is an option for changing text of messages, embeds and buttons. To do this, follow instructions below:
```bash
1. Download source code from the repository.
2. Open config.json file and change anything you want text.
3. Build docker image using Dockerfile: docker build -t YOUR_IMAGE_NAME
4. Go to Usage section to run your bot.
```

### Issues

If you got any issues, please, create an issue in this [repository](https://github.com/psychemisss/aqua-bugreports).

### To-do

- [x] Discord modal text configuration
- [ ] Notion fields configuration
- [ ] Reports numeration

### License

This project is licensed under the [License](LICENSE).
