Abrir en WSL la carpeta:
cd /mnt/c/PV/Code/AWSDeepRacer/JupyterNotebooks

Build Image:
docker build -t jupyter-notebook .

Run Container:
docker run -it --rm -p 8888:8888 jupyter-notebook

Entrar al link que aparece en los logs de la consola.
