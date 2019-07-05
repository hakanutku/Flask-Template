# Mindsite Backend

**İçinde şifrelerin olduğu `.env` dosyasını oluştur!**

Virtual environment oluştur

`python3 -m venv venv` veya `python -m venv venv`

Virtual environment'i aktif et.

Mac'te

`$ source venv/bin/activate`

Windows'ta

`cd venv/Scripts/`

`activate`

Gereksinimleri yükle

`pip3 install -r requirements.txt` veya `pip install -r requirements.txt`

`flask run`

Yeni blueprint eklemek için app klasörünün içinde klasör aç ve `__init__.py` ve `routes.py` dosyalarını oluştur.

`__init__.py` dosyasının içine:

```
from flask import Blueprint

bp = Blueprint('<Blueprint Name>', __name__)

from app.<Blueprint Name> import routes
```

`routes.py` dosyasında da `bp`'yi import edip route'ları yazmaya başlayabilirsin.
