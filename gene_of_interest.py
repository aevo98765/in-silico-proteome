import urllib.request, json
from operator import itemgetter


class GeneOfInterest:

    def poi_proteome(self, gene_name, organism):
        biogrid_access_key = ""

        url = "https://webservice.thebiogrid.org/interactions?searchNames=true&geneList=" + gene_name + "&includeInteractors=true&format=json&max=1000&includeInteractorInteractions=false&taxId=" + organism + "&accesskey=" + biogrid_access_key

        with urllib.request.urlopen(url) as url:
            datas = json.loads(url.read().decode())

        poi_proteome = set()

        for data in datas:
            a = datas[data]["OFFICIAL_SYMBOL_A"].upper()
            b = datas[data]["OFFICIAL_SYMBOL_B"].upper()
            poi_proteome.add(a)
            poi_proteome.add(b)

        print(gene_name, "has", len(poi_proteome), "number of hits in the in silico proteome. Please wait...")

        return poi_proteome

    def proteome_comparison(self, poi_proteome, organism):
        lists_in_common = []
        for gene in poi_proteome:
            url = url = "https://webservice.thebiogrid.org/interactions?searchNames=true&geneList=" + gene + "&includeInteractors=true&format=json&max=1000&includeInteractorInteractions=false&taxId=" + organism + "&accesskey=160c9d5820c29e02dca794cacdbdee5f"
            with urllib.request.urlopen(url) as url:
                datas = json.loads(url.read().decode())
            list_general = set()
            list_in_common = set()
            for data in datas:
                a = datas[data]["OFFICIAL_SYMBOL_A"].upper()
                b = datas[data]["OFFICIAL_SYMBOL_B"].upper()
                list_general.add(a)
                list_general.add(b)
                if a in poi_proteome and b in poi_proteome:
                    list_in_common.add(a)
                    list_in_common.add(b)
            length_of_list = len(list_in_common)
            try:
                proportion_in_common = len(list_in_common) / len(list_general)
            except:
                pass
            try:
                proportion_times_number_in_common = length_of_list * proportion_in_common
            except:
                pass

            lists_in_common.append((str(gene), length_of_list, proportion_times_number_in_common, list_in_common))

        sorted_lists_in_common = sorted(lists_in_common, key=itemgetter(2), reverse=True)

        return sorted_lists_in_common


















