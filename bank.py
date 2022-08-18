from importlib.resources import path
from requests import patch, get
from dataclasses import dataclass, asdict
from appconf import conf
import json

__api_version = "v1"
__baseUrl = f"https://unbelievaboat.com/api/{__api_version}/guilds/{conf.guild_id}/"

__default_headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": conf.tokens.unb
}


@dataclass
class __CashPayload:
    cash: int
    reason: str


async def __patch_reward(user_id, payload):
    patch(
        url=f"{__baseUrl}/users/{user_id}",
        json=json.dumps(asdict(payload)),
        headers=__default_headers
    )


async def reward_cash(user_id, cash):
    __patch_reward(user_id=user_id, payload=__CashPayload(
        cash=cash,
        reason="Cave reward"
    ))


async def weekly_claim(user_id):
    __patch_reward(user_id=user_id, payload=__CashPayload(
        cash=60_000,
        reason="Weekly claim"
    ))


async def buy_ticket(user_id):
    __patch_reward(user_id=user_id, payload=__CashPayload(
        cash=-60_000,
        reason="Ticket buy"
    ))


async def get_balance(user_id) -> int:
    response = get(
        url=f"{__baseUrl}/users/{user_id}",
        headers=__default_headers
    )
    return response.json()["cash"]
