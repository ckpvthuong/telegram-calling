### 1. installation
- ```apt install make cmake gcc g++ python3-dev gcc g++ openssl libssl-dev libopus0 libopus-dev```
- ```pip install -r requirements.txt```
- set var: API_ID, API_HASH, SESSION_NAME(option)
- replace ```chat_id``` in **main.py**

### 2. Run
- ```python main.py```

### 3. encode, decode voice
- ```ffmpeg -i input.mp3 -f s16le -ac 1 -ar 48000 -acodec pcm_s16le input.raw```  # encode
- ```ffmpeg -f s16le -ac 1 -ar 48000 -acodec pcm_s16le -i output.raw output.mp3```  # decode