import geopandas as gpd
from agile import agile
import os

descr = input("filename specification (e.g. 'missing6'): ")

GIST = gpd.read_file("../data/large_data/GIST_v0-1.geojson", driver="GeoJSON")
GIST.set_index("PHI_ID", inplace=True)

def lemmatize_with_agile(raw_text):
    try:
        doc = agile.lemmatize(raw_text)
        lemmata = [word["lemma"] for sent in doc.to_dict() for word in sent]
    except:
        lemmata = []
    return lemmata

def lemmata_by_phiid(phiid):
    lemmata = lemmatize_with_agile(GIST[GIST["PHI_ID"]==phiid]["clean_text_interpretive_word"].tolist()[0])
    id_with_lemmata = " ".join([str(phiid)] + lemmata)
    return id_with_lemmata


def preprocess_lemmata_txt(lemmata_full_str):
    lemmata_data_split =  [inscr_data.split() for inscr_data in lemmata_full_str.split("\n")]
    lemmata_data_tups = [(int(inscr_data[0]), inscr_data[1:]) for inscr_data in lemmata_data_split]
    lemmata_data_dict = dict(lemmata_data_tups)
    return lemmata_data_dict

filenames = os.listdir("../data/large_data/lemmata_files")

lemmata_full_merged = {}
for fname in filenames:
    lemmata_full_str = open("../data/large_data/lemmata_files/" + fname, "r", encoding="utf-8").read()
    lemmata_full_merged.update(preprocess_lemmata_txt(lemmata_full_str))

lemmatized_ids_set = set(lemmata_full_merged.keys())
missing_ids = list(set(GIST.index.symmetric_difference(lemmatized_ids_set)))

GIST_missing = GIST.loc[missing_ids]
GIST_missing.reset_index(inplace=True)

print("currently missing: ", len(GIST_missing))


f = open("../data/large_data/lemmata_files/lemmata_full_{}.txt".format(descr), "w", encoding="utf-8")

print("starting to write into file...")
for n in range(len(GIST_missing)):
    id = str(GIST_missing.iloc[n]["PHI_ID"])
    lemmata = lemmatize_with_agile(GIST_missing.iloc[n]["clean_text_interpretive_word"])
    line_data = " ".join([str(id)] + lemmata) + "\n"
    f.writelines(line_data)

#%%
