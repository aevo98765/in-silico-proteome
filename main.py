from gene_of_interest import GeneOfInterest
import sys


def gene_choice():
    gene_choice = input("Please enter the gene name of your protein of interest: ").upper()
    return gene_choice


def organism_choice():
    while (True):
        organism_choice = input("Pease enter the organism type (Human = 1, Mouse = 2, Rat = 3) (1-3): ")
        if organism_choice == "1":
            return ["Human", "9606"]
        elif organism_choice == "2":
            return ["Mouse", "10090"]
        elif organism_choice == "3":
            return ["Rat", "10116"]
        else:
            pass


gene_choice = gene_choice()
organism_choice = organism_choice()
gene1 = GeneOfInterest()

proteome_1 = gene1.poi_proteome(gene_choice, organism_choice[1])

list_in_common = gene1.proteome_comparison(proteome_1, organism_choice[1])

original_stout = sys.stdout
with open(gene_choice + "_" + organism_choice[0], "w") as f:
    sys.stdout = f
    print("1. Gene name.")
    print("2. Number of proteome hits in common.")
    print("3. Proteome hits in common relative to the proteome size.")
    print("4. A list of the proteome hits in common.")
    print("\n")
    print("---------------")
    print("\n")

    index = 0
    for gene in list_in_common:
        index += 1
        print(str(index) + ".", end=" ")
        for e in gene:
            print(e)
        print("\n")
        print("---------------")
        print("\n")
    sys.stdout = original_stout
    print("Complete! Check the files.")

