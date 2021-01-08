# Spam Samples Collector

An Telethon userbot that made to collect samples of spam and automating the process
of triggering `/fban` across Telegram for your bot federation.

## Getting Started

### GitLab Users
1. [Fork the repo](https://gitlab.com/ThePinsTeam-FedSupport/SpamSamplesCollector/-/forks/new) to the namespace you have access.
2. Sign in to Heroku, create an new app for your fork then generate an new API token (**Account Settings** -> **Applications**).
3. Open the **CI/CD Settings**, expand the **Variables** section, then add your app name as `HEROKU_APP_NAME` and your
API key as `HEROKU_PRODUCTION_KEY`.
4. Before deploying to Heroku, see the detailed configuration list below before editing strings or doing some code edits.

### GitHub
WIP.

### Self-hosting

Requires Python 3.x and Git during the initial setup. For updating, simply `git pull` (to pull code changes) and `./spsmcollector-cli install --virtualenv` (to update dependencies).

1. [Fork the repo](https://gitlab.com/ThePinsTeam-FedSupport/SpamSamplesCollector/-/forks/new) to the namespace you have access.
2. Clone your fork onto your machine.
3. Copy the `config.sample.py`, edit and save as `config.py`.
4. Install dependencies with `./spsmcollector-cli install --virtualenv`.
5. Depending on your operating system, run `start.sh` or `start.bat`.

## Configuration

| Environment Variable | Description | Type |
| --- | --- | --- |
| `ENV` | To enable env mode. | Boolean |
| `API_ID_KEY` | Telegram API app ID, generted from <https://my.telegram.org> | Interger |
| `API_HASH_KEY` | Telegram API app hash, generted from <https://my.telegram.org> | String |
| `STRING_SESSION` | String session, generated from the `spsmcollector-cli generate-string-session`. | String |
| `BOT_TOKEN` | Bot API token, generated from BotFather, for inline stuff | String |
| `HEROKU_API_KEY` | Heroku API key, generated from **Account Settings** -> **Applications**. | String | 
| `HEROKU_APP_NAME` | Your Heroku app slug. | String |
| `MONGO_DB_URL` | MongoDB URL, must be the 3.4+ URL format. | String |
| `SIBYL` | ID of Users who have full access to the userbot. | Intergers, speraated by spaces |
| `INSPECTORS` | ID of users who can force an approval on scans, can manage blacklists, etc. | Intergers, speraated by spaces |
| `ENFORCERS` | ID of users who can send ban requests. | Intergers, speraated by spaces |
| `Sibyl_logs` | Chat ID where ban requests are sent. | Interger
| `Sibyl_approved_logs` | Chat ID where approved requests are being logged. | Interger
| `GBAN_MSG_LOGS` | Chat ID where triggeres `/fban` command. | Interger

## Using the CLI

> Currently, the CLI is only available for Windows users with
Git Bash installed/WSL enabled and Linux users. We'll be working
to add native CLI support for Windows users in the future.

The `spsmcollector-cli` script is included to help you manage your SSC userbot easily. To get started, type `./spsmcollector-cli help` in terminal and press Enter to see possible commands.

## Credits

* Original repo where we forked: <https://github.com/AnimeKaizoku/SibylSystem>.
