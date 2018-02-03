# For:
# open input json file
# load json file into python dict object

from json import dump, load

# host
HOST = 'http://localhost:20001'

# load token json file
DATA_TOKEN = load(open('./data/supervisor/authorization/token.json'))


# http://api/dacdy.com/authorization/supervisor-sessions
URL_SUPERVISOR_SESSION = HOST + '/authorization/supervisor-sessions'
DATA_SUPERVISOR_SESSION = load(open('./data/supervisor/authorization/session.json', 'r'))

# htpp://api/dacdy.com/authorization/supervisors/sms
URL_SUPERVISOR_SMS = HOST + '/authorization/supervisors/sms'
DATA_SUPERVISOR_SMS = {
    "RESTPASSWORD": load(open('./data/supervisor/authorization/sms/resetpassword.json', 'r')),
    "BINDMOBILE": load(open('./data/supervisor/authorization/sms/bindmobile.json', 'r'))
}

# http://api/dacdy.com/authorization/supervisors/{supervisorId}/sms
supervisorId = '5a24c7107d3b0d1c18cdc729'
URL_SUPERVISOR_SUPERVISORID_SMS = HOST + '/authorization/supervisors/' + supervisorId + '/sms'
DATA_SUPERVISOR_SUPERVISORID_SMS = {
    "CHANGEPASSWORD":
    load(open('./data/supervisor/authorization/supervisorId_sms.json', 'r')),
    "RELEASEMOBILE":
    load(open('./data/supervisor/authorization/sms/supervisorid_releasemobile.json', 'r'))
}

# http://api/dacdy.com/authorization/reset-password
# URL_SUPERVISOR_SMS's smscode
supervisorId = '5a24c7107d3b0d1c18cdc729'
URL_SUPERVISOR_RESETPASSWORD = HOST + '/authorization/supervisors/reset-password'
DATA_SUPERVISOR_RESETPASSWORD = load(
    open('./data/supervisor/authorization/resetpassword.json', 'r'))

# http://api.dacdy.com/authorization/{supervisorId}/bind-mobile
# URL_SUPERVISOR_SMS's smscode
supervisorId = '5a24c7107d3b0d1c18cdc729'
URL_SUPERVISOR_SUPERVISORID_BINDMOBILE = HOST + '/authorization/supervisors/' + supervisorId + '/bind-mobile'
DATA_SUPERVISOR_SUPERVISORID_BINDMOBILE = load(
    open('./data/supervisor/authorization/supervisorId_bindmobile.json', 'r'))

# http://api.dacdy.com/authorization/supervisors/{supervisorId}/change-password
# URL_SUPERVISOR_SUPERVISORID_SMS's smscode
supervisorId = '5a24c7107d3b0d1c18cdc729'
URL_SUPERVISOR_SUPERVISORID_CHANGEPASSWORD = HOST + '/authorization/supervisors/' + supervisorId + '/change-password'
DATA_SUPERVISOR_SUPERVISORID_CHANGEPASSWORD = load(
    open('./data/supervisor/authorization/supervisorId_changepassword.json', 'r'))

# http://api.dacdy.com/authorizationsupervisors/{supervisorId}/create-worker
# URL_SUPERVISOR_SUPERVISORID_SMS's smscode
supervisorId = '5a24c7107d3b0d1c18cdc729'
URL_SUPERVISOR_SUPERVISORID_CREATEWORKER = HOST + '/authorization/supervisors/' + supervisorId + '/create-worker'
DATA_SUPERVISOR_SUPERVISORID_CREATEWORKER = load(
    open('./data/supervisor/authorization/supervisorId_createworker.json', 'r'))

# http://api.dacdy.com/authorization/supervisors/{supervisorId}/release-mobile
# URL_SUPERVISOR_SUPERVISORID_SMS's smscode
supervisorId = '5a24c7107d3b0d1c18cdc729'
URL_SUPERVISOR_SUPERVISORID_RELEASEMOBILE = HOST + '/authorization/supervisors/' + supervisorId + '/release-mobile'
DATA_SUPERVISOR_SUPERVISORID_RELEASEMOBILE = load(
    open('./data/supervisor/authorization/supervisorId_releasemobile.json', 'r'))

# http://api.dacdy.com/authorization/supervisors/{supervisorId}/maintain-worker/{workerId}
# URL_SUPERVISOR_SUPERVISORID_SMS's smscode
supervisorId = '5a24c7107d3b0d1c18cdc729'
workerId = '5a2e32276a7aba0001f56291'
URL_SUPERVISOR_SUPERVISORID_MAINTAINWORKER = HOST + '/authorization/supervisors/' + supervisorId + '/maintian-worker/' + workerId


# worker
URL_WORKER_SESSION = HOST + '/authorization/worker-sessions'
DATA_WORKER_SESSION = load(open('./data/woker/authorization/woker_session.json'))

URL_WORKER_SMS = HOST + '/worker/sms'
DATA_WORKER_SMS = load(open('./data/woker/authorization/resetpassword_sms.json'))

URL_WORKER_RESETPASSWORD = HOST + '/authorization/'
