<div align="center">
  <h1>🏹 <code>recon-bolt-proxy</code></h1>
  <p>
    <strong>Proxy server based on <a href="https://mitmproxy.org/">mitmproxy</a> that bypasses Riot Games ban of the Recon Bolt app for <a href="https://playvalorant.com/">Valorant</a></strong>
  </p>
</div>

## 🚢 Usage

Setting it up requires some technical knowledge, but it works on Windows, macOS, and Linux.
The container can be hosted on your computer or a Raspberry PI, almost anything that can run [Docker](https://www.docker.com/). 

1. Install [Docker](https://www.docker.com/)
1. Add the following content into a `docker-compose.yml` file:

```YAML
version: "3.9"
services:
  proxy:
    image: ghcr.io/kennethwussmann/recon-bolt-proxy:latest
    tty: true
    ports:
      - 8080:8080
      # Optional: For debugging enable webserver
      #- 8081:8081
```

2. Start the container with the command `docker compose up -d`. Run it in a terminal in the same directory as the file. Refer to [Docker Compose Guide](https://docs.docker.com/get-started/08_using_compose/) for more info.
3. Connect your iPhone to the proxy server

- Settings > WiFi > `<Your Network>` > Configure Proxy > Manual > [Enter IP of computer](https://support.microsoft.com/en-us/windows/find-your-ip-address-in-windows-f21a9bbc-c582-55cd-35e0-73431160a1b9) running proxy and port `8080`

4. Head over to [http://mitm.it](http://mitm.it) on your iPhone
5. Follow the instructions on that page (download certificate, install profile, trust certificate)
6. Done! The app will now load successfully again.

⭐ If you bought the Recon Bolt Pro features, they will work too!

> ‼️ You need to stay connected to the proxy to use the app (the widget works without the proxy)

> [!IMPORTANT]  
> You need to disable 2FA in your Riot Games account to continue using the Recon Bolt app. They stopped sending 2FA emails from the outdated app. 

## 😢 Background

See also: [Recon Bolt: Riot Shuts Down App](https://earlygame.com/valorant/bye-bye-recon-bolt-riot-shuts-down-app-due-to-instalocking)

Mid July Riot Games forced the developer of the Recon Bolt app to shut down and remove the app from the stores.
The app continued working for a few days for users who still had it installed, but then Riot Games also blocked requests coming from the app. Almost all parts of the app stopped working.

The for me most best part still works without proxy, the iOS widget, because it used a different User-Agent.

### 🔮 How the proxy works

Riot Games configured their CloudFlare to block requests coming from the Recon Bolt app based on it's User-Agent. The proxy uses mitmproxy to intercept and modify requests by the iOS app to change the User-Agent to something else.

It's packaged as a Docker image and can run locally on your computer when you want to use the app.

---

<sup><sub>
Riot Games™ and Valorant™ are trademarks or registered trademarks of Riot Games, Inc. This project is not affiliated with, endorsed, or sponsored by Riot Games, Inc., Valorant, or the Recon Bolt app.
The `recon-bolt-proxy` is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.
The usage of this proxy server may violate the terms of service of Riot Games or Valorant. Riot Games could detect the usage of Recon Bolt via this proxy and decide to ban your account. By using `recon-bolt-proxy`, you understand and accept these risks.
In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.
Remember, I'm not redistributing the app Recon Bolt. This proxy only works if you still happen to have Recon Bolt installed on your device right now. I don't guarantee that any of this works/continues to work.
The use of `recon-bolt-proxy` is at your own risk.
</sub></sup>
