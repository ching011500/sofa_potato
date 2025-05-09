FROM python:3.8-slim

# 安裝系統相依套件
RUN apt-get update && apt-get install -y \
    build-essential \
    swig \
    cmake \
    libffi-dev \
    libssl-dev \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# 安裝 auto-sklearn 和 jupyter notebook
RUN pip install --upgrade pip \
    && pip install auto-sklearn jupyter notebook

# 建立工作資料夾
WORKDIR /workspace

# 預設啟動 Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
