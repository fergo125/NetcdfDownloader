kill $(ps aux | grep 'java' | awk '{print $2}')
sh ./scripts/scriptCopernicus.sh
python3 ./scripts/Downloader.py
idv ./Plantillas/N
