from mitmproxy import http

class ModifyUserAgent:
    def __init__(self, new_user_agent):
        self.new_user_agent = new_user_agent

    def request(self, flow: http.HTTPFlow) -> None:
        user_agent = flow.request.headers.get('User-Agent', '')
        if 'Recon%20Bolt' in user_agent:
            flow.request.headers['User-Agent'] = self.new_user_agent

addons = [
    ModifyUserAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_8 rv:6.0) Gecko/20210828 Firefox/35.0")
]
