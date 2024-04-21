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

### Running a image in a container

> [!CAUTION]
> We can't have two containers with the same container name. Either you have to remove or rename the previous container to use the same name.

- -d : run container in background and print container ID (detach mode)
    - Otherwise if the container runs in the terminal, when we close the terminal it will stop. We won't be able to use the terminal while the container when the container is running if not for -d 
```sh
docker run --name <new-container-name> -d <image-name> 
```

- -p : publish a container's port(s) to the host
    - There are different default ports for different applications. For example, postgres default port is 5432. But, when we are spinning up multiple containers of the same image they should have different ports instead of the default port to avoid port conflicts.
```sh
docker run -d -p <host-port>:<container-port> --name <container-name> <image-name>
```

> [!NOTE]
> If you don't have a image that you need to use in the container, docker will automatically pull the relevant image for you.

> [!IMPORTANT]
> The command that used to run a image can be different from image to image depending on the image type. So we need to refer to the documentation of that specific image before running.

- For example when we need to run a postgres image in a container we need to pass some environment variables (-e) too.
    ```sh
        docker run --name <name> -e POSTGRES_PASSWORD=<password> -d postgres
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

### Removing a container
```sh
docker rm <container-name>
```
```sh
docker container rm <container-name>
```

### Remove all stopped containers
```sh
docker container prune
```

### Clean up all unused containers, images, volumes etc.
```sh
docker system prune
```





















