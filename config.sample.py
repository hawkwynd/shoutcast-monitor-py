# Rename to config.py and fill in the blanks 
# Set SID to your stream ID

sc = dict(
    host = 'http://yourshoutcastserver.com',
    port = ':8000',
    path = '/admin.cgi',
    passw = '&pass=yourAdminPassword',
    sid  = '?sid=1',
    mode = '&mode=viewjson'
)
