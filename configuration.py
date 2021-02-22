import secrets

# Campaign Manager
CM_app = secrets.CM_app
CM_user = secrets.CM_user
CM_password = secrets.CM_password
CM_base = 'https://api.modicagroup.com/rest/campaign_manager/v1/' + CM_app
CM_lists = CM_base + '/lists'
CM_managed_lists = ['testing']
