from config import LOG, EVENT_LOGS,
from FallenRobot import app
from FallenRobot.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
**{by- Tanu } ᴩʟᴀʏ ʟᴏɢɢᴇʀ**

**ᴄʜᴀᴛ:** {message.chat.title} [`{message.chat.id}`]
**ᴜsᴇʀ:** {message.from_user.mention}
**ᴜsᴇʀɴᴀᴍᴇ:** @{message.from_user.username}
**ɪᴅ:** `{message.from_user.id}`
**ᴄʜᴀᴛ ʟɪɴᴋ:** {chatusername}

**sᴇᴀʀᴄʜᴇᴅ ғᴏʀ:** {message.text}

**sᴛʀᴇᴀᴍ ᴛʏᴩᴇ:** {streamtype}"""
        if message.chat.id != EVENT_LOGS:
            try:
                await app.send_message(
                    EVENT_LOGS,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
