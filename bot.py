import twitchio
from twitchio.ext import commands
import random
import config


class Bot(commands.Bot):
    async def event_command_error(self, context: commands.Context, error: Exception):
        if isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.ArgumentParsingFailed):
            await context.reply(error.message)

        elif isinstance(error, commands.MissingRequiredArgument):
            await context.reply("Вам не хватает аргументов: " + error.name)

        elif isinstance(error, commands.CheckFailure): # we'll explain checks later, but lets include it for now.
            await context.reply("Извините, вы не можете выполнить эту команду: " + error.args[0])

        else:
            print(error)

    def __init__(self):
        super().__init__(token=config.TOKEN, prefix='=', initial_channels=["Art5507", "ToptunovyjBot"])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        
    
    # Команда =ping
    @commands.cooldown(rate=1, per=5, bucket=commands.Bucket.user)
    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.reply(f'🏓Понг! Топтуновый бот работает!')

    # Команда =help
    @commands.cooldown(rate=1, per=5, bucket=commands.Bucket.user)
    @commands.command(name="help")
    async def help(self, ctx: commands.Context):
        await ctx.reply(f'Информация о боте находится тут: https://tptnbot.vercel.app/')

    # Команда =random
    @commands.cooldown(rate=1, per=5, bucket=commands.Bucket.user)
    @commands.command(name="random")
    async def random(self, ctx: commands.Context, minimal: int, maximum: int):
        random_number = random.randint(minimal, maximum)
        await ctx.reply(f'{random_number}')

    # Команда =coin
    @commands.cooldown(rate=1, per=5, bucket=commands.Bucket.user)
    @commands.command(name="coin")
    async def coin(self, ctx: commands.Context):
        words_list = ["Орёл", "Решка"]
        random_word = random.choice(words_list)
        await ctx.reply(f'🪙 {random_word}')

    # Команда =lon
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="lon")
    async def lon(self, ctx: commands.Context):
        await ctx.reply(f'Лон ты скуф GAGAGA')

    # Команда =afk
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="afk")
    async def afk(self, ctx: commands.Context, message: str = None):
        if message == None:
            message = "(нет сообщения)"
        await ctx.reply(f'⛵ {ctx.author.mention} ушел в афк: {message}')

    # Команда =gn
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="gn")
    async def gn(self, ctx: commands.Context, message: str = None):
        if message == None:
            message = "(нет сообщения)"
        await ctx.reply(f'💤 {ctx.author.mention} ушел спать: {message}')

    # Команда =brb
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="brb")
    async def brb(self, ctx: commands.Context, message: str = None):
        if message == None:
            message = "(нет сообщения)"
        await ctx.reply(f'ppHop {ctx.author.mention} скоро вернется: {message}')

    # Команда =shower
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="shower")
    async def shower(self, ctx: commands.Context, message: str = None):
        if message == None:
            message = "(нет сообщения)"
        await ctx.reply(f'🚿 {ctx.author.mention} принимает душ: {message}')

    # Команда =food
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="food")
    async def food(self, ctx: commands.Context, message: str = None):
        if message == None:
            message = "(нет сообщения)"
        food_list = ["🍇", "🍈", "🍉", "🍊", "🍋", "🍌", "🍍", "🥭", "🍎", "🍏", "🍐", "🍑", "🍒", "🍓", "🫐", "🥝", "🍅", "🫒", "🥥", "🥑", "🍆", "🥔", "🥕", "🌽", "🌶️", "🫑", "🥒", "🥬", "🥦", "🧄", "🧅", "🥜", "🫘", "🌰", "🫚", "🫛", "🍞", "🥐", "🥖", "🫓", "🥨", "🥯", "🥞", "🧇", "🧀", "🍖", "🍗", "🥩", "🥓", "🍔", "🍟", "🍕", "🌭", "🥪", "🌮", "🌯", "🫔", "🥙", "🧆", "🥚", "🍳", "🥘", "🍲", "🫕", "🥣", "🥗", "🍿", "🧈", "🧂", "🥫", "🍱", "🍘", "🍙", "🍚", "🍛", "🍜", "🍝", "🍠", "🍢", "🍣", "🍤", "🍥", "🥮", "🍡", "🥟", "🥠", "🥡", "🦀", "🦞", "🦐", "🦑", "🦪", "🍦", "🍧", "🍨", "🍩", "🍪", "🎂", "🍰", "🧁", "🥧", "🍫", "🍬", "🍭", "🍮", "🍯", "🍼", "🥛", "☕", "🫖", "🍵", "🍶", "🍾", "🍷", "🍸", "🍹", "🍺", "🍻", "🥂", "🥃", "🫗", "🥤", "🧋", "🧃", "🧉", "🧊", "🥢", "🍽️", "🍴", "🥄", "🔪", "🫙", "🏺"]
        random_food = random.choice(food_list)    
        await ctx.reply(f'{random_food} {ctx.author.mention} сейчас ест: {message}')

    # Команда =lurk
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="lurk")
    async def lurk(self, ctx: commands.Context, message: str = None):
        if message == None:
            message = "(нет сообщения)"
        await ctx.reply(f'👥 {ctx.author.mention} сейчас скрывается: {message}')

    # Команда =poop
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="poop")
    async def poop(self, ctx: commands.Context, message: str = None):
        if message == None:
            message = "(нет сообщения)"
        await ctx.reply(f'🚽 {ctx.author.mention} сейчас какает: {message}')

    # Команда =work
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="work")
    async def work(self, ctx: commands.Context, message: str = None):
        if message == None:
            message = "(нет сообщения)"
        await ctx.reply(f'💼 {ctx.author.mention} работает: {message}')

    # Команда =study
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="study")
    async def study(self, ctx: commands.Context, message: str = None):
        if message == None:
            message = "(нет сообщения)"
        await ctx.reply(f'📚 {ctx.author.mention} сейчас учится: {message}')

    # Команда =nap
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="nap")
    async def nap(self, ctx: commands.Context, message: str = None):
        if message == None:
            message = "(нет сообщения)"
        await ctx.reply(f'😴 {ctx.author.mention} сейчас дремлет: {message}')

    # Команда =draw
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="draw")
    async def draw(self, ctx: commands.Context, message: str = None):
        if message == None:
            message = "(нет сообщения)"
        await ctx.reply(f'🖌️ {ctx.author.mention} сейчас рисует: {message}')

    # Команда =tuck
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="tuck")
    async def tuck(self, ctx: commands.Context, user: twitchio.PartialChatter, emote: str = None):
        if emote == None:
            emote = "Okay"
        await ctx.reply(f'Вы уложили {user.name} спать {emote} 👉 🛏️')

    # Команда =hug
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="hug")
    async def hug(self, ctx: commands.Context, user: twitchio.PartialChatter):
        await ctx.reply(f'Вы обняли {user.name} 🤗')

    # Команда =8ball
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="8ball")
    async def eightball(self, ctx: commands.Context):
        words_list = ["😃 Это несомненно.", "😃 Это решительно так.", "😃 Без сомнения.", "😃 Да - определенно.","😃 Вы можете на это положиться.", "😃 Как мне кажется, да.", "😃 Скорее всего.", "😃 Перспектива хорошая.", "😃 Да.", "😃 Признаки указывают на то, что да.", "😐 Ответ неясен, попробуйте еще раз.", "😐 Спросите позже.", "😐 Лучше не говорить вам сейчас", "😐 Невозможно предсказать сейчас.", "😐 Сконцентрируйтесь и спросите еще раз.", "😦 Не рассчитывайте на это.", "😦 Мой ответ - нет.", "😦 Мои источники говорят, что нет.", "😦 Перспективы не очень хорошие.", "😦 Очень сомнительно."]
        random_word = random.choice(words_list)
        await ctx.reply(f'{random_word}')

    # Команда =explosion
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="explosion")
    async def explosion(self, ctx: commands.Context):
        await ctx.reply(f'Art5507Explosion')

    # Команда =shdhdexplosion
    @commands.cooldown(rate=1, per=10, bucket=commands.Bucket.user)
    @commands.command(name="shdhdexplosion")
    async def shdhdexplosion(self, ctx: commands.Context):
        await ctx.reply(f'ShadowDemonHDExplosion')

bot = Bot()
bot.run()