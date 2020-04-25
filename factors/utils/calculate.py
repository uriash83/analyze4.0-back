import dateutil.parser

def formatDate(date):
    datetemp = dateutil.parser.isoparse(date)
    return datetemp.strftime("%Y-%m-%d")
