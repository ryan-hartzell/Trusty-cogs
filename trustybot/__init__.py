from .trustybot import TrustyBot


__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)


def setup(bot):
    n = TrustyBot(bot)
    bot.add_cog(n)
