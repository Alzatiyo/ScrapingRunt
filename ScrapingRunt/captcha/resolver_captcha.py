import tempfile
from anticaptchaofficial.imagecaptcha import imagecaptcha
from config.settings import ANTICAPTCHA_KEY

def resolver_captcha(img_bytes):

    solver = imagecaptcha()

    solver.set_verbose(1)
    solver.set_key(ANTICAPTCHA_KEY)
    solver.set_minLength(4)
    solver.set_maxLength(6)
    solver.set_case(True)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as f:
        f.write(img_bytes)
        temp_path = f.name


    texto = solver.solve_and_return_solution(temp_path)

    if texto != 0:
        print(f"Captcha resuelto: {texto}")
        return texto


    return None