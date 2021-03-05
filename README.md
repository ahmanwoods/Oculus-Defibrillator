# Oculus-Defibrillator
Fix for multiplayer when launching Oculus VR titles outside of the official client. 

The Oculus Platform API requires a "heartbeat" sent via the Oculus desktop client to enable multiplayer features. Currently, when launching Oculus applications outside of the desktop client without a valid headset configuration (eg, client reports pending hardware issue), the client doesnt report the correct current App ID in its heartbeat requests. This is the case when launching applications via compatibility layers such as Revive or PiTool. This incorrect App ID results in being removed from multiplayer parties with friends after a certain amount of time.
# Installation
1. Install Python
2. Install requests (pip install requests)
3. Configure script with game App ID. Can be found at on the Oculus store at: oculus(dot)com/experiences/rift/appid
# Usage
1. Start script
2. A response with "current_room_id" indicates it is working correctly
3. Script must be running while you're in game
4. ?????
5. Profit
