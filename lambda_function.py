from gene_of_interest import poi_proteome, proteome_comparison
from utilities import result_generation, send_mail

import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ)
    logger.info('## EVENT')
    logger.info(event)

    subject_string = event['gene_name'] + " results"
    proteome = poi_proteome(event['gene_name'], event['species_id'])
    list_in_common = proteome_comparison(proteome, event['species_id'])
    results = result_generation(event['gene_name'], event['species_id'], list_in_common)
    send_mail(event['email'], subject_string, results)

# event = {
#     'gene_name': 'Grik2',
#     'species_id': '9606',
#     'email': 'ashevans3@gmail.com'
# }
#
# if __name__ == "__main__":
#     lambda_handler(event, "")