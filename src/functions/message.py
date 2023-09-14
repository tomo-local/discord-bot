async def reply(message):
    reply = f"{message.author.mention} 読んだ？"
    await message.channel.send(reply)

    # コマンドに対応するリストデータを取得する関数を定義


async def slash_command(message):
    command = message.content
    data_table = {
        "/members": message.guild.members,  # メンバーのリスト
        "/roles": message.guild.roles,  # 役職のリスト
        "/text_channels": message.guild.text_channels,  # テキストチャンネルのリスト
        "/voice_channels": message.guild.voice_channels,  # ボイスチャンネルのリスト
        "/category_channels": message.guild.categories,  # カテゴリチャンネルのリスト
    }

    data = data_table.get(command, "無効なコマンドです")
    member_names = [member.name for member in data]

    for name in member_names:
        await message.channel.send(name)
