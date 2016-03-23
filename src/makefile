BUILD=../build/
DEST_HOST="root@10.4.12.24"
#DEST_HOST_STAGE="root@10.4.12.24"
DEST_DIR="/vz/private/215/var/www"
REMOVE_COMMAND="rm -rf /vz/private/215/var/www/*"
SRC=${BUILD}	

all:
	mkdir ${BUILD};rsync -avC --progress *  ${BUILD}
clean:
	rm -rf ${BUILD}

pull:
	git pull origin develop

stage:  pull 
	ssh -o "StrictHostKeyChecking no" ${DEST_HOST} ${REMOVE_COMMAND}
	rsync -avz --progress ${SRC} ${DEST_HOST}":"${DEST_DIR}

