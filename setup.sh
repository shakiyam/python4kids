#!/bin/bash
set -eu -o pipefail

sudo apt update
sudo apt install -y libsm6 libxrender1 python3-venv
python3 -m venv "$HOME"/python3
# shellcheck disable=SC1090
. "$HOME"/python3/bin/activate
cat >>"$HOME"/.bashrc <<EOT
# shellcheck disable=SC1090
. "$HOME"/python3/bin/activate
EOT
pip3 install --upgrade flake8 flake8-import-order flask opencv-python opencv-contrib-python
