from mitmproxy import http
import json


class ModifyUserAgentAndNonce:
    def __init__(self, new_user_agent):
        self.new_user_agent = new_user_agent

    def request(self, flow: http.HTTPFlow) -> None:
        # Modify User-Agent
        user_agent = flow.request.headers.get("User-Agent", "")
        if "Recon%20Bolt" in user_agent:
            flow.request.headers["User-Agent"] = self.new_user_agent

        # Modify nonce
        if flow.request.pretty_url.endswith("api/v1/authorization"):
            try:
                data = json.loads(flow.request.content)
                if "nonce" in data:
                    data["nonce"] = "1"
                    flow.request.content = json.dumps(data).encode("utf-8")
            except json.JSONDecodeError:
                pass  # not a JSON request


addons = [
    ModifyUserAgentAndNonce(
        "Mozilla/5.0 (Windows NT 10.3; WOW64) AppleWebKit/603.41 (KHTML, like Gecko) Chrome/48.0.2354.213 Safari/600",
    )
]
