import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
df = pd.read_excel('2021.01.28 - ANTALIS PACKAGING - Analyse scraping.xls')
#df
palette_quantile= ['cornflowerblue','grey','lightcoral']  # haut / moyen / bas
palette_media = ['lightseagreen','teal','darkslategrey'] # texte / image / vidéo

palette_quantile= ['cornflowerblue','grey','lightcoral']  # haut / moyen / bas
palette_media = ['lightseagreen','teal','darkslategrey'] # texte / image / vidéo


size_title = 28
size_label = 22
size_ticks = 20

x1 = 20
y1 = 30

x2 = 11
y2 = 11

x3 = 20
y3 = 30

point=8



### LONGUEUR
fig = plt.figure(figsize=(x1,y1))
fig.suptitle('   Par nombre de caractères                                       Par nombre de mots\n',fontsize=size_title, fontweight='bold')

## Visualisation par nombre de caractères
plt.subplot(321)
sns.barplot(y=df.groupby('score_pondere_quantile')[['longueur_post_car']].mean().index,x=df.groupby('score_pondere_quantile')['longueur_post_car'].mean().values,order=['haut','moyen','bas'],orient='h',palette=palette_quantile);
plt.xlabel('\nLongueur moyenne des posts (nombre de caractères)',size=size_label);
plt.ylabel("Niveau d'engagement",size=size_label);
plt.xticks(fontsize=size_ticks)
plt.yticks(fontsize=size_ticks)
plt.title("Longueur moyenne des posts \nen fonction du niveau d'engagement\n",size=size_title)

plt.subplot(323)
sns.boxplot(x=df.longueur_post_car,y=df.score_pondere_quantile,orient='h',order=['haut','moyen','bas'],palette=palette_quantile);
plt.xlabel('\nLongueur des posts (nombre de caractères)',size=size_label);
plt.ylabel("Niveau d'engagement",size=size_label);
plt.xticks(fontsize=size_ticks)
plt.yticks(fontsize=size_ticks)
plt.title("Longueur des posts \nen fonction du niveau d'engagement\n",size=size_title)

plt.subplot(325)
sns.stripplot(x=df.longueur_post_car,y=df.score_pondere_quantile,orient='h',order=['haut','moyen','bas'],palette=palette_quantile,s=point);
plt.xlabel('\nLongueur des posts (nombre de caractères)',size=size_label)
plt.ylabel("Niveau d'engagement",size=size_label);
plt.xticks(fontsize=size_ticks)
plt.yticks(fontsize=size_ticks)
plt.title("Longueur des posts \nen fonction du niveau d'engagement\n",size=size_title)


## Visualisation par nombre de mots
plt.subplot(322)
sns.barplot(y=df.groupby('score_pondere_quantile')[['longueur_post_word']].mean().index,x=df.groupby('score_pondere_quantile')['longueur_post_word'].mean().values,order=['haut','moyen','bas'],orient='h',palette=palette_quantile);
plt.xlabel('\nLongueur moyenne des posts (nombre de mots)',size=size_label);
plt.ylabel("Niveau d'engagement",size=size_label);
plt.xticks(fontsize=size_ticks)
plt.yticks(fontsize=size_ticks)
plt.title("Longueur moyenne des posts \nen fonction du niveau d'engagement\n",size=size_title)

plt.subplot(324)
sns.boxplot(x=df.longueur_post_word,y=df.score_pondere_quantile,orient='h',order=['haut','moyen','bas'],palette=palette_quantile);
plt.xlabel('\nLongueur des posts (nombre de mots)',size=size_label);
plt.ylabel("Niveau d'engagement",size=size_label);
plt.xticks(fontsize=size_ticks)
plt.yticks(fontsize=size_ticks)
plt.title("Longueur des posts \nen fonction du niveau d'engagement\n",size=size_title)

plt.subplot(326)
sns.stripplot(x=df.longueur_post_word,y=df.score_pondere_quantile,orient='h',order=['haut','moyen','bas'],palette=palette_quantile,s=point);
plt.xlabel('\nLongueur des posts (nombre de mots)',size=size_label);
plt.ylabel("Niveau d'engagement",size=size_label);
plt.xticks(fontsize=size_ticks)
plt.yticks(fontsize=size_ticks)
plt.title("Longueur des posts \nen fonction du niveau d'engagement\n",size=size_title)

fig.tight_layout(pad=8)
st.pyplot(fig, transparent=True)


import multiprocessing
from playsound import playsound

p = multiprocessing.Process(target=playsound, args=("/Users/valentinpasquier/Downloads/streamlit_test/Oval.mp3",))
p.start()
input("press ENTER to stop playback")
p.terminate()