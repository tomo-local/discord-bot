from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.hybrid_command(name="load", hidden=True)
    @commands.is_owner()
    async def load(self, ctx: commands.Context, *, cog: str):
        await ctx.defer(ephemeral=True)

        cogs = f"cogs.{cog}"

        try:
            await self.bot.load_extension(cogs)
            await self.bot.tree.sync()

        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send(content="**`LOAD SUCCESS`**", ephemeral=True)

    @commands.hybrid_command(name="unload", hidden=True)
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, *, cog: str):
        await ctx.defer(ephemeral=True)
        cogs = f"cogs.{cog}"

        try:
            await self.bot.unload_extension(cogs)
            await self.bot.tree.sync()

        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")

        else:
            await ctx.send("**`UNLOAD SUCCESS`**", ephemeral=True)

    @commands.hybrid_command(name="reload", hidden=True)
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, *, cog: str):
        await ctx.defer(ephemeral=True)

        cogs = f"cogs.{cog}"

        try:
            await self.bot.reload_extension(cogs)
            await self.bot.tree.sync()

        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("**`RELOAD SUCCESS`**", ephemeral=True)


async def setup(bot) -> None:
    await bot.add_cog(Admin(bot))
