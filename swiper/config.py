"""
第三方配置
"""
# 互亿无限短信配置
HY_SMS_URL = 'http://106.ihuyi.com/webservice/sms.php?method=Submit'
HY_SMS_PARAMS = {
    'account': 'C468545021',
    'password': '60c5157972c733cae505ff4e71f6922e',
    'content': '您的验证码是：%s。请不要把验证码泄露给其他人。',
    'mobile': None,
    'format': 'json'
}


# 七牛云配置
QN_ACCESS_KEY = 'h9jPcV5T14ujBUOwoYePqpY64wAhFv0XKymUORr_'
QN_SECRET_KEY = '67ExnldaNT0valK9U4bOQIaDyQ3-DTPfoCf_oKsO'
QN_BUCKET_NAME = 'swiper-test'
QN_BASE_URL = 'http://rgz4dtvve.hn-bkt.clouddn.com'