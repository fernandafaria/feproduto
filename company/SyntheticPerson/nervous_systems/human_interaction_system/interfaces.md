# Interfaces — Human Interaction System

Pub: human.* events. Sub: response-ready events from agents/systems,
governance disclosure policy, product changelogs, narrative messages.

Channels: web, email, chat, voice, programmatic API. Each channel has a
documented disclosure profile.

API:
```
POST /human/inbound {channel, content, identity}
GET /human/satisfaction
GET /human/consents/{user_id}
POST /human/consent_revoke {user_id}
```
