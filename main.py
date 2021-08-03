import asyncio
import os

from tgvoip import VoIPServerConfig
from tgvoip_pyrogram import VoIPFileStreamService, VoIPNativeIOService
import pyrogram

# replace chat_id
chat_id = '@thuongpham4869'

session_name = os.environ.get('SESSION_NAME', 'my_account')
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

VoIPServerConfig.set_bitrate_config(80000, 100000, 60000, 5000, 5000)
client = pyrogram.Client(session_name, api_id, api_hash)
loop = asyncio.get_event_loop()
voip_service = VoIPFileStreamService(client, receive_calls=False)  # use VoIPNativeIOService for native I/O

async def main():
    await client.start()

    call = await voip_service.start_call(chat_id)
    call.play('input.raw')
    call.play_on_hold(['input.raw'])
    call.set_output_file('output.raw')

    @call.on_call_state_changed
    def state_changed(call, state):
        print('State changed:', call, state)


    @call.on_call_ended
    async def call_ended(call):
        await asyncio.sleep(1)
        await client.stop()
        print("call ended")
        global in_call
        in_call = False

    global in_call
    while in_call:
        await asyncio.sleep(1)

in_call = True
loop.run_until_complete(main())
