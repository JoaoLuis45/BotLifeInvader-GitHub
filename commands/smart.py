from discord.ext import commands

class Smart(commands.Cog):
    """Works with calcs"""
    def __init__(self,bot) :
        self.bot = bot

    #FUNÇÃO QUE RETORNA O VALOR FINAL DA QUANTIDADE DE DINHEIRO APOS O DOMINAS
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        if "dominas" in message.content:
            ds = message.content.split()
            menos = int(ds[1]) / 200000 * 30000
            response = int(ds[1]) - menos
            await message.channel.send(f"R${int(ds[1])} de dinheiro sujo equivale a: R${response} de dinheiro limpo!")

    @commands.command(name="calcular",help="Comando para calcular expressões, requer dois argumentos!")
    async def calculate_expression(self,ctx,*expression):
        expression = ''.join(expression)
        response = eval(expression)
        await ctx.send("A resposta é: " + str(response))

def setup(bot):
    bot.add_cog(Smart(bot))
