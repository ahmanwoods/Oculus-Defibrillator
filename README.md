# This fix is now built into revive
This script is no longer needed as Revive now has this functionality built in as of version 2.0. Simply sign into the Revive dashboard using your Oculus information and the rest is done for you.
# Oculus-Defibrillator
Fix for multiplayer when launching Oculus VR titles outside of the official client. The Oculus Platform API requires a "heartbeat" sent via the Oculus desktop client to enable multiplayer features. Currently, when launching Oculus applications outside of the desktop client without a valid headset configuration (eg, client reports pending hardware issue), the client doesnt report the correct current App ID in its heartbeat requests. This is the case when launching applications via compatibility layers such as Revive or PiTool.
# Configuration
1. Install Python
2. Install requests (pip install requests)
3. Acquire your Oculus desktop client OAuth token. Can be found under access_token in the body of graph.oculus.com requests. Fiddler is a good application for this. Enabling HTTPS Decryption is required.
4. Configure script with OAuth token.
5. Configure script with game App ID. Can be found at on the Oculus store at: oculus(dot)com/experiences/rift/appid
# Usage
1. Start script with python oculus_heartbeat.py
2. A response with "current_room_id" indicates it is working correctly
3. Script must be running while you're in game
4. ?????
5. Profit
