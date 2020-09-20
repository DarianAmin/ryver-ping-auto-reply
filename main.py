import pyryver
import asyncio
async def main():
    # Connect to ryver
    async with pyryver.Ryver("Organization_Name", "Username", "Password") as ryver:
        # Load all chats
        await ryver.load_chats()
        # Connect to the websockets interface
        async with ryver.get_live_session() as session:
            @session.on_chat
            async def on_message(msg: pyryver.WSChatMessageData):
                # Makes sure to check that the message isn't from the bot itself
                from_user = ryver.get_user(jid=msg.from_jid)
                me= ryver.get_user(username="Username")
                if "@Username".lower() in msg.text and from_user.get_username() != "Username":
                    chat = ryver.get_chat(jid=msg.from_jid) 
                    #replies to the ping
                    await chat.send_message("This is an automated response\nHi There! Thanks for your ping.I will respond to your message as soon as possible.")
                    print("Ping reply triggered by " +from_user.get_username())
                    await me.send_message("You have been pinged by "+from_user.get_username())
                    await me.send_message("The message was "+msg.text+"\n")
                    await me.send_message(" ")



            @session.on_connection_loss
            async def on_connection_loss():
                await session.close()

            # run until session.close() is called
            await session.run_forever()

asyncio.get_event_loop().run_until_complete(main())
