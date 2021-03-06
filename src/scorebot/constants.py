#!/usr/bin/false
#
# Scorebotv4 - The Scorebot Project
# 2018 iDigitalFlame / The Scorebot / CTF Factory Team
#
# Scorebot Secondary Constants

HOST_IP = '127.0.0.1'
HOST_VALUE = 100
FLAG_VALUE = 100
SERVICE_VALUE = 100
CONTENT_VALUE = 100


GAME_STATUS = (
    (0, 'Stopped'),
    (1, 'Running'),
    (3, 'Paused'),
    (4, 'Completed'),
    (5, 'Archived')
)
GAME_MODES = (
    (0, 'Red vs Blue'),
    (1, 'Blue vs Blue'),
    (2, 'King'),
    (3, 'High Ground')
)
GAME_RUNNING = 1

GAME_SETTING_DEFAULT = {
    'job_timeout': 300,
    'ping_tolerance': 75
}

SERVICE_STATUS = (
    (0, 'red'),
    (1, 'yellow'),
    (2, 'green')
)
SERVICE_PROTOCOLS = (
    (0, 'tcp'),
    (1, 'udp'),
    (2, 'icmp')
)
SERVICE_STATUS_LOOKUP = {
    'red': 0,
    'yellow': 1,
    'green': 2
}

CORRECTION_REASONS = (
    (0, 'Unknown'),
    (1, 'Scoring Error'),
    (2, 'Invalid Score Issued')
)

AUTHORIZATION_NAMES = {
    'TESTING': 0,
    'MONITOR': 1
}

SCORE_SUBCLASS = (
    (0, 'Transaction'),
    (1, 'Payment'),
    (2, 'Transfer'),
    (3, 'Purchase'),
    (4, 'Correction'),
    (5, 'PaymentHealth'),
    (6, 'TransferResult'),
    (7, 'TransactionFlag'),
    (8, 'TransactionBeacon')
)
SCORE_SUBCLASS_TRANSACTION = 0
SCORE_SUBCLASS_PAYMENT = 1
SCORE_SUBCLASS_TRANSFER = 2
SCORE_SUBCLASS_PURCHASE = 3
SCORE_SUBCLASS_CORRECTION = 4
SCORE_SUBCLASS_PAYMENTHEALTH = 5
SCORE_SUBCLASS_TRANSFERRESULT = 6
SCORE_SUBCLASS_TRANSACTIONFLAG = 7
SCORE_SUBCLASS_TRANSACTIONBEACON = 8

TEAM_SUBCLASS = (
    (0, 'Team'),
    (1, 'ScoreTeam'),
    (2, 'PlayerTeam')
)
TEAM_TOKEN_DAYS = 10
TEAM_SUBCLASS_TEAM = 0
TEAM_SUBCLASS_SCORETEAM = 1
TEAM_SUBCLASS_PLAYERTEAM = 2
TEAM_DEFAULT_FIELD = 'token'
TEAM_DEFAULT_TOKEN_DAYS = 10
TEAM_DEFAULT_LOGO = 'default.png'

FLAG_MESSAGE_HINT = '{{"result": "\'{hint}\'"}}'
FLAG_MESSAGE_NOT_EXIST = '{"result": "SBE4: Flag does not exist!"}'
FLAG_MESSAGE_STOLEN = '{"result": "SBE4: Flag was already stolen!"}'

HOST_MESSAGE_INVALID_IP = '{"result": "SBE4: Beacon address is invalid!}'
HOST_MESSAGE_NO_HOST = '{"result": "SBE4: No Host with that address exists!}'
HOST_MESSAGE_BEACON_EXISTS = '{"result": "SBE4: Host currently has an active Beacon!"}'

TEAM_MESSAGE_TOKEN = '{{"token": "{token}"}}'
TEAM_MESSAGE_PORT_LIST = '{{"ports": [{list}]}}"'
TEAM_MESSAGE_PORT = '{{"result": "Port \'{port}\' Opened!}}"'
TEAM_MESSAGE_EXPIRED = '{"result": "SBE4: Team Token is expired!"}'
TEAM_MESSAGE_PORT_INVALID = '{"result": "SBE4: Invaid Port Number!}"'
TEAM_MESSAGE_MISSING_FIELD = '{{"result": "SBE4: Field \'{field}\' is missing!"}}'
TEAM_MESSAGE_NO_TEAM = '{"result": "SBE4: Team with matching Token does not exist!"}'
TEAM_MESSAGE_NOT_OFFENSIVE = '{"result": "SBE4: Team with matching Token is not marked as Offensive!"}'

MESSAGE_INVALID_FORMAT = '{"result": "SBE4: Invalid JSON format!"}'
MESSAGE_GAME_NO_RUNNING = '{"result": "SBE4: Game is not running!"}'
MESSAGE_INVALID_METHOD = '{"result": "SBE4: Not a supported method type!"}'
MESSAGE_MISSING_FIELD = '{{"result": "SBE4: Missing field value \'{field}\'!"}}'
MESSAGE_INVALID_ENCODING = '{"result": "SBE4: Invalid encoding, UTF-8 is required!"}'

JOB_MESSAGE_PASSED = '{"result": "SBE4: Job Accepted"}'
JOB_MESSAGE_INVALID_JOB = '{"result": "SBE4: Invalid Job Data!"}'
JOB_MESSAGE_NOT_MONTIOR = '{"result": "SBE4: Not a Monitor Token!"}'
JOB_MESSAGE_NO_MONTIOR = '{"result": "SBE4: Invalid Monitor Token!"}'
JOB_MESSAGE_NO_HOSTS = '{"result": "SBE4: No current valid Hosts available!"}'
JOB_MESSAGE_NO_GAMES = '{"result": "SBE4: Not assigned to any running Games!"}'

AUTHENTICATE_MESSAGE_INVALID = '{"result": "SBE4: Invalid HTTP Headers!"}'
AUTHENTICATE_MESSAGE_NO_HEADER = '{"result": "SBE4: No Authentication Header Found!"}'
AUTHENTICATE_MESSAGE_INVALID_TOKEN = '{"result": "SBE4: Invalid Authentication Token!"}'
AUTHENTICATE_MESSAGE_EXPIRED = '{"result": "SBE4: Authentication Token is expired or invalid!"}'
AUTHENTICATE_MESSAGE_MISSING_PERM = '{{"result": "SBE4: Authentication Token missing the \'{perm}\' permission!"}}'

# EOF
