from gene_of_interest import poi_proteome, proteome_comparison
from utilities import result_generation, send_mail


def lambda_handler(event, context):
    subject_string = event['gene_name'] + " results"
    proteome = poi_proteome(event['gene_name'], event['species_id'])
    list_in_common = proteome_comparison(proteome, event['species_id'])
    results = result_generation(event['gene_name'], event['species_id'], list_in_common)
    send_mail(event['email'], subject_string, results)

