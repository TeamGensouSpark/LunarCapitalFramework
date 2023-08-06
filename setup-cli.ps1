python -m pip install --upgrade pip
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pdm
pdm config pypi.url https://pypi.tuna.tsinghua.edu.cn/simple
python -m pdm self update
pdm install