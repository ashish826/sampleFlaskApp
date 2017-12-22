rm -rf sampleFlaskApp
git clone https://github.com/ashish826/sampleFlaskApp
cd sampleFlaskApp
whoami
/usr/local/bin/pip install -r requirements.txt
cat app.py
ls -lrt
docker build -t ashish826/sampleflaskapp .
docker push ashish826/sampleflaskapp


