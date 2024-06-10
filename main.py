import discord
from discord.ext import commands
import google.generativeai as genai

# Correct the typo in the variable name
DISCORD_TOKEN = ''
GEMINI_API_KEY = ''

genai.configure(api_key=GEMINI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True  # Use the correct intent
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command(name='ai')
async def query(ctx, *, question):
    if not question:
        await ctx.send("Please provide a query")
        return

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(question)

        # Ensure correct referencing of response text
        if response and hasattr(response, 'text'):
            response_text = response.text
            for chunk in [response_text[i:i + 1900] for i in range(0, len(response_text), 1900)]:
                await ctx.send(chunk)
        else:
            await ctx.send("No valid response from the model.")
    except Exception as e:
        await ctx.send(f"An error occurred while processing your request: {e}")


bot.run(DISCORD_TOKEN)
