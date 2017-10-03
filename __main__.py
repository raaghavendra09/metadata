from metadata import metadata_reckoner, operationaldata_reckoner, hive_manager

import sys
import sys,getopt

def help():
    help_statement = "The METADATA job has to be started using the following protocols: \n\n\n" \
                     "  Metadata Ingestion           : python metadata-XXX.egg --job=M \n \n  Operational Data Ingestion   : python metadata-XXX.egg --job=O --status=0 --jobtype=ingestion  \n\n" \
                     "  Creation of hive tables      : python metadata-XXX.egg --job=create-hive \n \n  Help                         : python metadata-XXX.egg --help \n\n " \
                     " Status : 0 - STARTED, 1 - RUNNING, 2 - SUCCESS \n Jobtype : Ingestion, Transformation, Consumption, Curation"
    return help_statement



if __name__ == "__main__":

    job = ''
    status = 0
    ingestion_param = []

    options, remainder = getopt.getopt(sys.argv[1:], 'o:h', ['job=','status=', 'jobtype=','help'])

    for opt, arg in options:

        if opt in ('-j', '--job'):
            job = arg
        elif opt in ('-s', '--status'):
            status = arg
        elif opt in ('-s', '--jobtype'):
            ingestion_param =  arg.split(",")
        elif opt in ('-h', '--help'):
            print "\n\n\n HELP \n\n\n"
            print help()
            sys.exit()
        else:
            print "\n\n\n HELP \n\n\n"
            print help()
            sys.exit()

    if job == 'M':
        metadata_reckoner.start_main(ingestion_param)
    elif job == 'O':
        operationaldata_reckoner.start_main(status, ingestion_param)
    elif job == 'create-hive':
        hive_manager.start_main(sys.argv[1:])
    else:
        print "\n\n Metadata Ingestion cannot start with options - " + job + "\n\n"
        print help()
        sys.exit()



# if __name__ == "__main__":
#
#     status = "0"
#     ingestion_param = ['ingestion']
#     operationaldata_reckoner.start_main(status, ingestion_param)



