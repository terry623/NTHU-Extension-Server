import tempfile
import requests
import subprocess
from PIL import Image
import io


def tesseract(path):
    return subprocess.check_output([
        'tesseract',
        path, '-',
        '-psm', '8',
        '-c', 'tessedit_char_whitelist=0123456789', 'nobatch'
    ]).strip()


def preprocess(b):
    color = Image.open(io.BytesIO(b))
    gray = color.convert('L')
    bw = gray.point(lambda c: (c > 150) * 255, '1')
    fp = io.BytesIO()
    bw.save(fp, 'png', dpi=(70, 70))
    return fp.getvalue()


def decaptcha_url(url, params=None):
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmpimg:
        tmpimg.write(preprocess(requests.get(url, params=params).content))
        tmpimg.flush()
        return tesseract(tmpimg.name).replace(b' ', b'')


# print(decaptcha_url(
#     'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/mod/auth_img/auth_img.php',
#     params={'ACIXSTORE': '1b3u3vq7m8qsqmnq3n9avdsuj7'}
# ))
