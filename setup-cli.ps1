cd script/lunar-cli
python -m pip install --upgrade pip
pip install -i https://mirror.sjtu.edu.cn/pypi/web/simple pdm
pdm config pypi.url https://mirror.sjtu.edu.cn/pypi/web/simple
python -m pdm self update
pdm install
cd ../..
pause