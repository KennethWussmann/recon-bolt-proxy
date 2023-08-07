# recon-bolt-proxy

Proxy server based on [mitmproxy](https://mitmproxy.org/) that bypasses Riot Games ban of the Recon Bolt App for Valorant.

## Usage

The container can be hosted on your computer or a Raspberry PI, almost anything that can run [Docker](https://www.docker.com/).

1. Setup using Docker Compose:

```YAML
version: "3.9"
services:
  proxy:
    image: #TODO
    tty: true
    ports:
      - 8080:8080
      # Optional: For debugging enable webserver
      #- 8081:8081
```

2. Connect your iPhone to the proxy server

- Settings > WiFi > `<Your Network>` > Configure Proxy > Manual > Enter IP of server running proxy and port `8080`

3. Head over to [http://mitm.it](http://mitm.it)
4. Follow the instructions on that page (download certificate, install profile, trust certificate)
5. Done! The will now load successfully again.

⭐ If you bought the Recon Bolt Pro features, they will work too!

> ‼️ You need to stay connected to the proxy to use the app (the widget works without the proxy)

## Background

See also: [Recon Bolt: Riot Shuts Down App](https://earlygame.com/valorant/bye-bye-recon-bolt-riot-shuts-down-app-due-to-instalocking)

Mid July Riot Games forced the developer of the Recon Bolt app to shut down and remove the app from the stores.
The app continued working for a few days for users who still had it installed, but then Riot Games also blocked requests coming from the app. Almost all parts of the app stopped working.

The for me most best part still works without proxy, the iOS widget, because it used a different User-Agent.

### How the proxy works

Riot Games configured their CloudFlare to block requests coming from the Recon Bolt app based on it's User-Agent. The proxy uses mitmproxy to intercept and modify requests by the iOS App to change the User-Agent to something else.

It's packaged as a Docker image and can run locally in your computer when you want to use the app.

## Disclaimer

I'm not redistributing the app Recon Bolt. This proxy only works if you still happen to have Recon Bolt installed on your device right now. I don't guarantee that any of this works/continues to work.

I also don't include anything from Riot Games or Valorant. I don't support instalocking, but I do liked the app as a companion with additional stats and guides and that's what I use it for personally.

This is provided at your own risk. Riot Games can see that you still use Recon Bolt via this proxy and may decide to ban your account.
