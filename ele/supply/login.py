class loginEle(object):
    def __init__(self, *args):
        super(loginEle, self).__init__(*args)
        
    
    loginEle = {
        "username":"//input[@id='viewhigh-login-username-input']",
        "password":"//input[@id='viewhigh-login-pwd-input']",
        "loginButton":"//button/span[normalize-space(text())='登录']"
    }

    