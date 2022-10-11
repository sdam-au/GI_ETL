import geopandas as gpd
from agile import agile
import os
import unicodedata

descr = input("filename specification (e.g. 'missing6'): ")

inverse = input("inverse?")
inverse = eval(inverse)

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


def normalize_encoding(string):
    return unicodedata.normalize("NFC", string)

def preprocess_lemmata_txt(lemmata_full_str):
    failed_ids = []
    lemmata_data_split =  [normalize_encoding(inscr_data).split() for inscr_data in lemmata_full_str.split("\n")]
    #lemmata_data_tups = [(int(inscr_data[0]), inscr_data[1:]) for inscr_data in lemmata_data_split]
    lemmata_data_tups = []
    for inscr_data in lemmata_data_split:
        if len(inscr_data) > 1:
            lemmata_data_tups.append((int(inscr_data[0]), inscr_data[1:]))
        else:
            try:
                failed_ids.append(int(inscr_data[0]))
            except:
                failed_ids.append(inscr_data)
    lemmata_data_dict = dict(lemmata_data_tups)
    return lemmata_data_dict, failed_ids


filenames = os.listdir("../data/large_data/lemmata_files")

lemmata_full_merged = {}
failed_ids = []
for fname in filenames:
    lemmata_full_str = open("../data/large_data/lemmata_files/" + fname, "r", encoding="utf-8").read()
    file_dict, file_failed_ids = preprocess_lemmata_txt(lemmata_full_str)
    failed_ids.extend(file_failed_ids)
    lemmata_full_merged.update(file_dict)

failed_ids = [el for el in failed_ids if isinstance(el, int)]

lemmatized_ids_set = set(list(lemmata_full_merged.keys()) + failed_ids)
missing_ids = list(set(GIST.index.symmetric_difference(lemmatized_ids_set)))

GIST_missing = GIST.loc[missing_ids]
GIST_missing.reset_index(inplace=True)

print("currently missing: ", len(GIST_missing))


f = open("../data/large_data/lemmata_files/lemmata_full_{}.txt".format(descr), "w", encoding="utf-8")



print("starting to write into file...")
for n in range(len(GIST_missing)):
    if inverse == True:
        id = str(GIST_missing.iloc[len(GIST_missing) -1 - n]["PHI_ID"])
        lemmata = lemmatize_with_agile(GIST_missing.iloc[len(GIST_missing) -1 - n]["clean_text_interpretive_word"])
    else:
        id = str(GIST_missing.iloc[n]["PHI_ID"])
        lemmata = lemmatize_with_agile(GIST_missing.iloc[n]["clean_text_interpretive_word"])
    line_data = " ".join([str(id)] + lemmata) + "\n"
    f.writelines(line_data)

#%%
