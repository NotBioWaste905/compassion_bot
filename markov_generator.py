import markovify
import pandas as pd
from sklearn import cluster

df = pd.read_parquet("questions.parquet")

texts_cl_1 = ''
texts_cl_2 = ''
texts_cl_3 = ''
texts_cl_4 = ''

for i in df[df["cluster"] == '0']["answer"]:
    texts_cl_1 += '\n' + i

for i in df[df["cluster"] == '1']["answer"]:
    texts_cl_2 += '\n' + i

for i in df[df["cluster"] == '2']["answer"]:
    texts_cl_3 += '\n' + i

for i in df[df["cluster"] == '3']["answer"]:
    texts_cl_4 += '\n' + i

model_cluster_1 = markovify.Text(texts_cl_1)
model_cluster_2 = markovify.Text(texts_cl_2)
model_cluster_3 = markovify.Text(texts_cl_3)
model_cluster_4 = markovify.Text(texts_cl_4)

def gen(cluster):
    out = None
    while out == None:
        out = cluster.make_sentence()
    return out