from random_username.generate import generate_username

class Username:
    def __init__(self, user_message, bot_send):
        self.user_message = user_message
        self.bot_send = bot_send
    async def check(self):
        if str(self.user_message).startswith('cuy/username'):
            await self.bot_send(f"nih cuy username nya ***{generate_username(1)[0]}***")
