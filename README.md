# I'm a Docker Beginner

### Official Documentation:

[Docker Reference](https://docs.docker.com/reference/)

[Docker Beginners Guide](https://docs.docker.com/get-started/overview/)

> Docker is a Containerization Tool.

We don't need a virtual machine in order to use docker. (Used to need)

Now, the docker desktop app handles the virtualization for you. 

Docker doesn't contain the whole kernel of the virtual machine, just the minimum configuration and enough OS layer that application needs bare minimum to run. Whenever it's required to something, it communicates with the host kernel.

So Docker is super speed and uses very little resources compared to VMs.

## Containers
> Containers are like the machines we used to run our disks.

We can setup a sandbox environment in a computer which do not interact with the outside environment just easily, and it's just a stand alone computer.

Using images we can boot up them and load up all the things it's called a container. 

Containers exposes ports to the outside world in order to communicate. We do port-mapping for that.

## Images
> Images are like disks (cd/dvd) we used to run applications.

We can pull public images of different applications without event signing in to [docker hub](https://hub.docker.com). 

But in order to,
-  push our images into docker hub or for something like AWS 
- to pull private images 

we need to sign in to [docker hub](https://hub.docker.com).

> [!NOTE]
> When you are pulling an image , it will be downloaded as layers. So, when the images are need to be updated, only the specific layers that got updates will be updated.

## Volumes
> This is a volume (disk space) that is spined up for containers to use for their tasks.
- For example, a container of a postgres image requires somewhere to store the database.

---

# Docker Commands

For More Information : [Docker CLI References](https://docs.docker.com/reference/cli/docker/)

### Docker base command ( shows the commands list )
```sh
docker
```

### Versions of components
```sh
docker version
```

### CLI version 
```sh
docker -v
```
```sh
docker --version
```

### Pull a image or a repository

This will pull the latest images of that type
```sh
docker pull <image-name>
```

If you want to set a specific version 
```sh
docker pull <image-name>:<version>
```

When the image is not a docker official image, you would need to use the following format
```sh
docker push <docker-id>/<image-name>
```

### Base Command for Docker images (shows the command list)
```sh
docker image
```

### Base Command for Docker images (shows the command list)
```sh
docker container
```

### Base Command for Docker images (shows the command list)
```sh
docker volume
```

### Get the list of all images
```sh
docker image ls
```

### Get the list of all running containers
```sh
docker ps
```
```
docker container ls
```

### Get the list of all containers (both running and stopped)
```sh
docker ps -a
```
```
docker container ls -a
```

### Creating a container and Running an image

> [!CAUTION]
> We can't have two containers with the same container name. Either you have to remove or rename the previous container to use the same name.

- `-d` : run container in background and print container ID (detach mode)
    - Otherwise if the container runs in the terminal, when we close the terminal it will stop. We won't be able to use the terminal while the container when the container is running if not for -d 
```sh
docker run --name <new-container-name> -d <image-name> 
```

- `-p` : publish a container's port(s) to the host
    - There are different default ports for different applications. For example, postgres default port is 5432. But, when we are spinning up multiple containers of the same image they should have different ports instead of the default port to avoid port conflicts. 
    - We need to map the container's port into a port in the host machine.
```sh
docker run -d -p <host-port>:<container-port> --name <container-name> <image-name>
```

> [!NOTE]
> If you don't have a image that you need to use in the container, docker will automatically pull the relevant image for you.

> [!IMPORTANT]
> The command that used to run a image can be different from image to image depending on the image type. So we need to refer to the documentation of that specific image before running.

- For example when we need to run a postgres image in a container we need to pass some environment variables (-e) too.
    ```sh
        docker run --name <name> -e POSTGRES_PASSWORD=mysecretpassword -d postgres
    ```

### Stopping a running container
```sh
docker stop <container-name> 
```
```sh
docker stop <container-ID>
```
```sh
docker container stop <container-name> 
```
```sh
docker container stop <container-ID>
```
> [!NOTE]
> As long as another container doesn't have the same initial letters as a container, we can use first few initial letters without using the whole ID.

### Restart a container 
```sh
docker restart <container-name> 
```
```sh
docker container restart <container-name>
```

### Removing a container
```sh
docker rm <container-name>
```
```sh
docker container rm <container-name>
```
```sh
docker container remove <container-name>
```

### Removing a image
```sh
docker rmi <image-name>
```
```sh
docker image rm <image-name>
```
```sh
docker image remove <image-name>
```

### Removing a volume
```sh
docker volume rm <image-name>
```
```sh
docker volume remove <image-name>
```

### Remove all stopped containers
```sh
docker container prune
```

### Remove unused images
```sh
docker image prune
```

### Remove unused local volumes
```sh
docker volume prune
```

### Clean up all unused containers, images, volumes, networks etc.
```sh
docker system prune
```

### Docker Logs
```sh
docker logs <container-name>
```
> [!NOTE]
> There are multiple options for logs like `--details`, `--follow` and `--since` etc. 

## Connecting multiple containers

### Docker networks base command ( shows the commands list )
```sh
docker network
```
> [!NOTE]
> You can create , connect , disconnect and prune networks using `docker network` commands.

### Getting a list of all networks
```sh
docker network ls
```

# Multicontainer Applications

## Using CLI Commands

Here, we are trying to connect a mongo container with a mongo-express container.

Mongo-express image is a Web-based MongoDB admin interface, written with Node.js and express. This is a pre-build image that we can get from the docker-hub.

We can spin up two containers each of them running mongo image and mongo-express image and try to create a network between them.

Both, containers must be in the same network in order to work.

You can connect your own applications that are running in containers to the mongo container just like this too.

We need to create a network first.
```sh
docker network create mongo-network
```
> [!IMPORTANT]
> When you are pasing multiple environment variables into a `docker run` command you need to use `-e` multiple times as above.

Then, we are creating a mongo container and add the network to it. (using `--net`)
``` sh
docker run -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password --name mongodb --net mongo-network -d mongo
```

Now, we need to create the mongo-express container in the same network as the mongo container.
> [!NOTE]
> You can use `\` in the terminal inorder to go to the next line or the terminal without terminating the currently writing command.

```sh
docker run -d \
> -p 8081:8081 \
> -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
> -e ME_CONFIG_MONGODB_PASSWORD=password \
> -e ME_CONFIG_MONGODB_SERVER=mongodb \
> --net mongo-network \
> --name mongo-express \
> mongo-express
```
> [!CAUTION]
> The `ME_CONFIG_MONGODB_SERVER` is very important here. We need to give the same name we gave to container that runs the mongo image. (mongodb)

> [!NOTE]
> Here, we are giving a host port that is same as the container port beacuse we are trying to connect the mongo container to a pre-build mongo-express container which might be connected using the mongo default port 27017. Also we need to pass inthrough multiple environment variables inorder to initialize a mongodb. Same goes to mongo-express on 8081 port.

## Docker Compose

By using docker compose we can spin up multiple docker containers at the same time using docker files.

### Docker compose base command ( shows the commands list )
```sh
docker compose
```

We need to create a `docker-compose.yaml` file. 

> [!NOTE]
> If you want you can call this file any name. But this is the standard.

> [!TIP]
> Refer to the `docker-compose.yaml` file.

### Using a docker-compose file to create containers
> [!WARNING]
> You need to be in the same directory as the `docker-compose.yaml` file in order to run this command.
```sh
docker compose -f <file-name> up
```

>[!IMPORTANT]
> **Dockerfiles are used to build Docker images, docker-compose files are used to define and manage multi-container Docker applications, providing a higher level of abstraction for container orchestration and management**

## Deploying a application using Docker (Python Flask)

We need to create a `Dockerfile` file here. 

> [!TIP]
> Refer to the Flask-App-Deployment folder.

### Build a image from a Dockerfile and push it into dockerhub

First we are going to build the image from the `Dockerfile`

`-t` : Username of the docker hub

:0.0.1.RELEASE : This is to indicate the version of the image (You can use latest or just ignore the version aswell)

>[!CAUTION]
> Remember to add the . at the end. That indicated that the image is build according to the Dockerfile in the current directory.

```sh
docker build -t itzzjb/hey-python-flask:0.0.1.RELEASE .
```

Then we need to check whether the image can be run properly. Just create a basic container to check.

```sh
docker container run -d -p 3000:3000 itzzjb/hey-python-flask:0.0.1.RELEASE
```

Now, we know that the image is working as expected. So, we can push it to the dockerhub.
```sh
docker push itzzjb/hey-python-flask:0.0.1.RELEASE
```

## Deploying a application using Docker (NodeJs API)

We need to create a `Dockerfile` file here. 

> [!TIP]
> Refer to the NodeJs-API-Deployment folder.

### Build a image from a Dockerfile and push it into dockerhub

First, we need to initialize the NodeJs Project. This generates the `package.json` file.

```sh
npm init
```

Then, do the following changes in `package.json` file.

```sh
"scripts": {
    "start": "node index.js"
},
```

Now, create a `index.js` file in the same directory. Write the program you need to write there.

After that, we need to install **Expressjs** (This helps to quickly create rest apis).
We used that to create the api program we wrote in `index.js` file.

```sh
npm install express
```

You can check whether the  application is working by,

```sh
node index.js
```









































