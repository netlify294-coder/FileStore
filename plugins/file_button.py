from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.pyromod import ListenerTimeout

#===============================================================#

@Client.on_message(filters.command('filebutton') & filters.private)
async def file_button_command(client: Client, message: Message):
    if message.from_user.id not in client.admins:
        return await message.reply("❌ Only admins can use this command!")

    current_text = getattr(client, 'file_btn_text', '') or "Not set"
    current_url = getattr(client, 'file_btn_url', '') or "Not set"

    status_msg = f"""<b>›› ᴄᴜsᴛᴏᴍ ꜰɪʟᴇ ʙᴜᴛᴛᴏɴ sᴇᴛᴛɪɴɢs</b>

<blockquote>ᴛʜɪs ʙᴜᴛᴛᴏɴ ɪs sʜᴏᴡɴ ʙᴇʟᴏᴡ ᴇᴠᴇʀʏ ꜰɪʟᴇ ᴅᴇʟɪᴠᴇʀᴇᴅ ᴠɪᴀ ʙᴀᴛᴄʜ/sɪɴɢʟᴇ ʟɪɴᴋs.
ᴄᴜʀʀᴇɴᴛ ᴛᴇxᴛ: {current_text}
ᴄᴜʀʀᴇɴᴛ ᴜʀʟ: {current_url}</blockquote>"""

    buttons = [
        [InlineKeyboardButton('✏️ sᴇᴛ ʙᴜᴛᴛᴏɴ', 'set_file_btn')],
        [InlineKeyboardButton('🗑 ʀᴇᴍᴏᴠᴇ ʙᴜᴛᴛᴏɴ', 'remove_file_btn')]
    ]
    await message.reply(status_msg, reply_markup=InlineKeyboardMarkup(buttons))


@Client.on_callback_query(filters.regex('^set_file_btn$'))
async def set_file_btn(client: Client, query):
    if query.from_user.id not in client.admins:
        return await query.answer('❌ Only admins can use this!', show_alert=True)

    await query.answer()
    await query.message.edit_text(
        "<b>sᴇɴᴅ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ᴛᴇxᴛ</b> (e.g. `Join Our Channel`) in the next 60 seconds:"
    )

    try:
        text_res = await client.listen(user_id=query.from_user.id, filters=filters.text, timeout=60)
        btn_text = text_res.text.strip()

        await text_res.reply(
            "<b>ɴᴏᴡ sᴇɴᴅ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʟɪɴᴋ</b> (must start with https:// or http://) in the next 60 seconds:"
        )
        url_res = await client.listen(user_id=query.from_user.id, filters=filters.text, timeout=60)
        btn_url = url_res.text.strip()

        if not (btn_url.startswith('https://') or btn_url.startswith('http://')):
            return await url_res.reply(
                "<b>✗ ɪɴᴠᴀʟɪᴅ ʟɪɴᴋ! ᴍᴜsᴛ sᴛᴀʀᴛ ᴡɪᴛʜ https:// ᴏʀ http://</b>\n\nRun /filebutton to try again."
            )

        client.file_btn_text = btn_text
        client.file_btn_url = btn_url
        await client.mongodb.update_file_button_setting('text', btn_text)
        await client.mongodb.update_file_button_setting('url', btn_url)

        await url_res.reply(
            f"<b>✓ ʙᴜᴛᴛᴏɴ ᴜᴘᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ!</b>\n\n<b>Text:</b> {btn_text}\n<b>URL:</b> {btn_url}\n\nIt'll now appear below every file sent via links."
        )
    except ListenerTimeout:
        await query.message.reply("<b>✗ ᴛɪᴍᴇᴅ ᴏᴜᴛ!</b> Run /filebutton to try again.")


@Client.on_callback_query(filters.regex('^remove_file_btn$'))
async def remove_file_btn(client: Client, query):
    if query.from_user.id not in client.admins:
        return await query.answer('❌ Only admins can use this!', show_alert=True)

    client.file_btn_text = ''
    client.file_btn_url = ''
    await client.mongodb.update_file_button_setting('text', '')
    await client.mongodb.update_file_button_setting('url', '')

    await query.answer('✓ Button removed!', show_alert=True)
    await query.message.edit_text("<b>✓ ᴄᴜsᴛᴏᴍ ꜰɪʟᴇ ʙᴜᴛᴛᴏɴ ʀᴇᴍᴏᴠᴇᴅ!</b>\n\nRun /filebutton to set a new one.")
