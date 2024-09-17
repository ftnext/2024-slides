# /// script
# dependencies = ["httpx", "rich"]
# ///
import httpx
from rich.pretty import pprint

resp = httpx.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
