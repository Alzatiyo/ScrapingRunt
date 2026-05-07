from anticaptchaofficial.recaptchav2proxyless import *
from config.settings import ANTICAPTCHA_KEY


def solve_recaptcha(site_key, url):

    solver = recaptchaV2Proxyless()

    solver.set_key(ANTICAPTCHA_KEY)

    solver.set_website_url(url)
    solver.set_website_key(site_key)

    result = solver.solve_and_return_solution()

    if result != 0:
        return result
    else:
        raise Exception("Captcha no resuelto")