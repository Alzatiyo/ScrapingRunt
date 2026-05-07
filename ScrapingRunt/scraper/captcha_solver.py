from anticaptchaofficial.recaptchav2proxyless import *
from config.settings import ANTICAPTCHA_KEY


def resolver_captcha(site_key, url):

    solver = recaptchaV2Proxyless()

    solver.set_key(ANTICAPTCHA_KEY)

    solver.set_website_url(url)
    solver.set_website_key(site_key)

    token = solver.solve_and_return_solution()

    if token != 0:
        return token
    else:
        raise Exception("Captcha no resuelto")