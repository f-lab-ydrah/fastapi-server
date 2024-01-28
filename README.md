# fastapi-server

# pyenv 설치 방법
```brew install pyenv```

```pyenv install --list```

ModuleNotFoundError: No module named '_lzma'
WARNING: The Python lzma extension was not compiled. Missing the lzma lib?

```brew install readline xz```

# pyenv로 파이썬 버전 설치
```pyenv install 3.12.0```

# pyenv로 python 버전 글로벌 설정
```pyenv global 3.12.0```

```
pyenv shell 3.12.0
pyenv: shell integration not enabled. Run `pyenv init' for instructions.
pyenv init
# Load pyenv automatically by appending
# the following to 
# ~/.zprofile (for login shells)
# and ~/.zshrc (for interactive shells) :

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Restart your shell for the changes to take effect.
```

# pyenv로 해당 폴더 파이썬 버전 설정
```pyenv local 3.12.0```

# pyenv 실행
```pyenv shell 3.12.0```

# pyenv 설치된 파이썬 버전 확인
```pyenv versions```

# 파이썬 버전 확인
```python --version```

---

# Poetry 설치 방법
```curl -sSL https://install.python-poetry.org | python3 -```

zsh: command not found: poetry
open ~/.zshrc
export PATH=$HOME/.local/bin:$PATH
source ~/.zshrc
poetry --version

poetry init
This command will guide you through creating your pyproject.toml config.

Package name [fastapi-server]:  
Version [0.1.0]:  0.0.1
Description []:  fastAPI REST API server
Author [kij <8bithermitcrab@gmail.com>, n to skip]:  kij
License []:  
Compatible Python versions [^3.11]:  3.12.0

Would you like to define your main dependencies interactively? (yes/no) [yes] yes
You can specify a package in the following forms:
  - A single name (requests): this will search for matches on PyPI
  - A name and a constraint (requests@^2.23.0)
  - A git url (git+https://github.com/python-poetry/poetry.git)
  - A git url with a revision (git+https://github.com/python-poetry/poetry.git#develop)
  - A file path (../my-package/my-package.whl)
  - A directory (../my-package/)
  - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Package to add or search for (leave blank to skip): 
Would you like to define your development dependencies interactively? (yes/no) [yes] yes
Package to add or search for (leave blank to skip): 

Generated file

[tool.poetry]
name = "fastapi-server"
version = "0.0.1"
description = "fastAPI REST API server"
authors = ["kij"]
readme = "README.md"

[tool.poetry.dependencies]
python = "3.12.0"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes

---

# poetry 가상환경 실행
```poetry shell```

# poetry에서 fastapi 패키지 설치
```poetry add fastapi```

# poetry 종료
```exit```

# fastAPI 서버 실행
```uvicorn main:app --reload```

# fastAPI 서버 실행 시, uvicorn 오류 날 때
zsh: command not found: uvicorn

```pip install uvicorn```

# fastAPI 서버 종료
ctrl + c