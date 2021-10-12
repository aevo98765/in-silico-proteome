import json
import requests
from operator import itemgetter



def poi_proteome(gene_name: str, organism: str):
    biogrid_access_key = "160c9d5820c29e02dca794cacdbdee5f"

    url = "https://webservice.thebiogrid.org/interactions?searchNames=true&geneList=" + gene_name + "&includeInteractors=true&format=json&max=1000&includeInteractorInteractions=false&taxId=" + organism + "&accesskey=" + biogrid_access_key

    response = requests.get(url)
    datas = response.json()

    poi_proteome = {}

    for data in datas:
        a = datas[data]["OFFICIAL_SYMBOL_A"].upper()
        b = datas[data]["OFFICIAL_SYMBOL_B"].upper()
        poi_proteome[a] = 1
        poi_proteome[b] = 1

    print(gene_name, "has", len(poi_proteome), "number of hits in the in silico proteome. Please wait...")

    return poi_proteome

def proteome_comparison(poi_proteome, organism):
    lists_in_common = []
    for gene in poi_proteome:
        url = "https://webservice.thebiogrid.org/interactions?searchNames=true&geneList=" + gene + "&includeInteractors=true&format=json&max=1000&includeInteractorInteractions=false&taxId=" + organism + "&accesskey=160c9d5820c29e02dca794cacdbdee5f"
        with urllib.request.urlopen(url) as url:
            datas = json.loads(url.read().decode())
        gene_dict = {}
        list_in_common = set()
        for data in datas:
            a = datas[data]["OFFICIAL_SYMBOL_A"].upper()
            b = datas[data]["OFFICIAL_SYMBOL_B"].upper()
            gene_dict[a] = 1
            gene_dict[b] = 1
            if a in poi_proteome and b in poi_proteome:
                list_in_common.add(a)
                list_in_common.add(b)
        length_of_list = len(list_in_common)
        try:
            proportion_in_common = len(list_in_common) / len(gene_dict)
        except:
            pass
        try:
            proportion_times_number_in_common = length_of_list * proportion_in_common
            proportion_times_number_in_common = round(proportion_times_number_in_common, 2)
        except:
            pass

        lists_in_common.append((str(gene), length_of_list, proportion_times_number_in_common, list_in_common))

    sorted_lists_in_common = sorted(lists_in_common, key=itemgetter(2), reverse=True)

    return sorted_lists_in_common

















