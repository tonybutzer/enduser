Image=tbutzer/etm_docker_image

hello:
	echo hello - did you mean make build instead or make publish
publish:
	#git remote set-url origin git@github.com:tonybutzer/enduser.git
	git remote set-url origin https://github.com/tonybutzer/enduser.git
	git config --global user.email tonybutzer@gmail.com
	git config --global user.name tonybutzer
	git config --global push.default simple
	git add .
	git commit -m "automatic git update from Makefile"
	git push


docker-enable:
	#sudo groupadd docker
	sudo usermod -aG docker ubuntu

build:
	docker build -t ${Image} .

run:
	docker run -it ${Image} bash

exec:
	docker exec -it ${Image} bash

images:
	docker image ls
	echo ================================================================================
	docker image ls | grep greg
