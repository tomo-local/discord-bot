async def reply(message):
    reply = f"{message.author.mention} 読んだ？"
    await message.channel.send(reply)

    # コマンドに対応するリストデータを取得する関数を定義
