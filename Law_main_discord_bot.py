import discord
from pprint import pprint
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json


def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

def get_dataset():
    df = pd.read_csv('Law봇/결과/+law_bot_main.csv' ,encoding='CP949')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()


class MyClient(discord.Client):
    async def on_ready(self):
        game = discord.Game("민사, 행정판례 공부") #VSC - Python
        await client.change_presence(status=discord.Status.online, activity=game)
        print('Logged on as', self.user)

    async def on_message(self, message):

        if message.author == self.user:
            return

        user_input=message.content
        
        embedding = model.encode(user_input)

        df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
        answer = df.loc[df['distance'].idxmax()]
        
        print('법률', answer['법률'])
        print('법원', answer['법원'])
        print('판결번호', answer['판결번호'])
        print('판결날짜', answer['판결날짜'])
        print('유사한사건', answer['유저'])
        print('결론', answer['챗봇'])
        print('죄목', answer['죄목'])
        print('유사도', answer['distance'])
        
        embed=discord.Embed(title="가상 판결", description="", color=0x588afe)
        embed.set_author(name="법원")
        embed.add_field(name="죄목: ", value=answer['죄목'], inline=True)
        embed.add_field(name="판결번호: ", value=answer['판결번호'], inline=True)
        embed.add_field(name="유사한사건", value=answer['유저'], inline=False)
        embed.add_field(name="결론", value=answer['챗봇'], inline=True)
        embed.add_field(name="법률", value=answer['법률'], inline=False)
        embed.set_footer(text="판결날짜: "+answer['판결날짜']+' - '+answer['판결번호'])
        await message.channel.send(embed=embed)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('토큰입력')
