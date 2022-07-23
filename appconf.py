from dataclasses import dataclass
from os import environ as env
from dotenv import load_dotenv


@dataclass
class Cooldowns:
    ticket: int
    cave: int


@dataclass
class Tokens:
    discord: str
    unb: str


@dataclass
class AppConf:
    cooldowns: Cooldowns
    tokens: Tokens
    command_prefix: str
    guild_id: str
    command_channel: int
    claim_channel: int
    add_money_channel: int


load_dotenv()
conf = AppConf(
    cooldowns=Cooldowns(
        cave=env.get("cavecooldown"),
        ticket=env.get("claimcooldown")
    ),
    tokens=Tokens(
        discord=env.get("token"),
        unb=env.get("unbtoken")
    ),
    command_prefix=env.get("commandprefix"),
    guild_id=env.get("serverid"),
    command_channel=env.get("commandchannelid"),
    claim_channel=env.get("claimchannelid"),
    add_money_channel=env.get("responsechannelid"),
)
