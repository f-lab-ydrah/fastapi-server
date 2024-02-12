# fastapi-server

## 다이어그램
[![](https://mermaid.ink/img/pako:eNptUlFLwlAU_iuX-7SBUuLbCKHQIhAytCevD3fbTYfubmx3SYgQ5kOhQUFFiIZBL0GCSUG_Sa__oTOnaNSezvm-c77vO9sa2HBMhjWs1xyjGteZoIQjeAynFtjcR8moDdzETpHg3dwhkp3X-eM1koO7WeeL4FJKCVwVuczzHZ5QFGU51XqXvTf5fEuwqqrIdOr8j0LvXk5GC4WQVgmPvBZRNKYtrTfTJNYQdS2QK4JeiRC-T30BJVTTSVd2-tPvCyQvB7L9oeSO8gUVbSH5Mp73uspBJuqunuTwQcmdRF1rJId9JZ3JZgoZFSKtfXyXGmzdmnoRLiym90LX_HHWEiwJJ5bQr2QoHk_B6OYaQATPbsZy8Dlvj1fHw8QGtnyl4TKIRNuMmziGbebZ1DLhQzVCmGBRYTYjWIOSs0B4tEZwLKJOa07dqFBPhHQjUiHYo7yah1ssXg7x5HZsxXD4A_5njMA7W5ro1Ld8gkOmSXgTItFAOPlzbmBNeAGL4cA1qWBpi5Y9akdg8wd3Qtep?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNptUlFLwlAU_iuX-7SBUuLbCKHQIhAytCevD3fbTYfubmx3SYgQ5kOhQUFFiIZBL0GCSUG_Sa__oTOnaNSezvm-c77vO9sa2HBMhjWs1xyjGteZoIQjeAynFtjcR8moDdzETpHg3dwhkp3X-eM1koO7WeeL4FJKCVwVuczzHZ5QFGU51XqXvTf5fEuwqqrIdOr8j0LvXk5GC4WQVgmPvBZRNKYtrTfTJNYQdS2QK4JeiRC-T30BJVTTSVd2-tPvCyQvB7L9oeSO8gUVbSH5Mp73uspBJuqunuTwQcmdRF1rJId9JZ3JZgoZFSKtfXyXGmzdmnoRLiym90LX_HHWEiwJJ5bQr2QoHk_B6OYaQATPbsZy8Dlvj1fHw8QGtnyl4TKIRNuMmziGbebZ1DLhQzVCmGBRYTYjWIOSs0B4tEZwLKJOa07dqFBPhHQjUiHYo7yah1ssXg7x5HZsxXD4A_5njMA7W5ro1Ld8gkOmSXgTItFAOPlzbmBNeAGL4cA1qWBpi5Y9akdg8wd3Qtep)

## 버전 목록
- pyenv : 2.3.35
- python : 3.12.0
- poetry : 1.7.1
- fastapi : 0.109.0
- uvicorn = 0.27.0

## 환경 설정 방법
### 1. pyenv 설치 방법
```brew install pyenv```

### 2. pyenv로 파이썬 버전 설치
```pyenv install 3.12.0```

### 3. pyenv 실행
```pyenv shell 3.12.0```

### 4. poetry 설치 방법
```curl -sSL https://install.python-poetry.org | python3 -```

### 5. poetry 가상환경 실행
```poetry shell```

### 6. poetry에서 패키지 설치
```poetry add fastapi```

### 7. poetry 종료 방법
```exit```

## fastAPI 서버 실행 및 종료 방법

### 1. 실행 방법
```uvicorn main:app --reload```

### 2. 종료 방법
```ctrl + c```