python -m venv .venv  
source .venv/bin/activate  

logfire auth  
logfire projects use rtgpu  

docker build -t rtgpu-image .  
docker run --env-file=.env -d --name rtgpu-container -p 8080:5000 rtgpu-image