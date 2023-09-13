async def reply(message):
    reply = f"{message.author.mention} 読んだ？"
    await message.channel.send(reply)

    # コマンドに対応するリストデータを取得する関数を定義


def get_data(message):
    command = message.content
    data_table = {
        "/members": message.guild.members,  # メンバーのリスト
        "/roles": message.guild.roles,  # 役職のリスト
        "/text_channels": message.guild.text_channels,  # テキストチャンネルのリスト
        "/voice_channels": message.guild.voice_channels,  # ボイスチャンネルのリスト
        "/category_channels": message.guild.categories,  # カテゴリチャンネルのリスト
    }
    return data_table.get(command, "無効なコマンドです")
