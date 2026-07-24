# RDXMUSIC Final Build

## जरूरी सुरक्षा बदलाव
- `reload.py` startup से disabled: यह token, Mongo URI और string session दिखाता था।
- `dev.py` disabled: remote Python/shell execution देता था।
- `pornplay.py` disabled.
- केवल reviewed music/admin plugins load होंगे।
- automatic git pull और runtime pip install disabled है।

## Required environment variables
`API_ID`, `API_HASH`, `BOT_TOKEN`, `MONGO_DB_URI`, `OWNER_ID`, `LOGGER_ID`, `STRING_SESSION`

## Telegram permissions
Bot और assistant दोनों को target group में add करें। Bot को admin और assistant को voice chat join permission दें। Assistant को LOGGER_ID वाले private group में add करना जरूरी है।

## Docker deploy
Repository connect करके Dockerfile deployment चुनें। अलग build command नहीं। Start command manually मांगे तो `python3 -m RDXMUSIC` दें।

## Test order
1. Logs में `Reviewed plugins loaded successfully` देखें।
2. Logs में `RDX Music started successfully` देखें।
3. Group voice chat start करें।
4. `/play song name`, `/pause`, `/resume`, `/skip`, `/end` चलाएं।

## Security
पुराना Spotify client secret revoke करें। पुराने bot tokens/string sessions अगर कभी public/shared हुए हों तो regenerate करें। `.env` GitHub पर upload न करें।
