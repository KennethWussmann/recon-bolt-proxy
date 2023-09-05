from mitmproxy import http

class ModifyUserAgent:
    def __init__(self, new_user_agent):
        self.new_user_agent = new_user_agent

    def request(self, flow: http.HTTPFlow) -> None:
        user_agent = flow.request.headers.get('User-Agent', '')
        if 'Recon%20Bolt' in user_agent:
            flow.request.headers['User-Agent'] = self.new_user_agent

addons = [
    ModifyUserAgent("Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 10.0; Trident/7.0)")
]
