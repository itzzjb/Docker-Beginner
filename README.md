# I'm a Docker Beginner

### Official Documentation:

[Docker Reference](https://docs.docker.com/reference/)

[Docker Beginners Guide](https://docs.docker.com/get-started/overview/)

> Docker is a Containerization Tool.

We don't need a virtual machine in order to use docker. (Used to need)

Now, the docker desktop app handles the virtualization for you.

### Containers
> Containers are like the machines we used to run our disks.

We can setup a sandbox environment in a computer which do not interact with the outside environment just easily, and it's just a stand alone computer. 

Using images we can boot up them and load up all the things it's called a container. 

### Images
> Images are like disks (cd/dvd) we used to run applications.

We can pull public images of different applications without event signing in to [docker hub](https://hub.docker.com). 

But in order to,
-  push our images into docker hub or for something like AWS 
- to pull private images 

we need to sign in to [docker hub](https://hub.docker.com).

> [!NOTE]
> When you are pulling an image , it will be downloaded as layers. So, when the images are need to be updated, only the specific layers that got updates will be updated.


### Volumes


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
docker --version
```

### Pull a image of a repository

This will pull the latest images of that type
```sh
docker pull <image-name>
```

If you want to set a specific version 
```sh
docker pull <image-name>:<version>
```

For most of the images you would need to use the following format
```sh
docker push <docker-id>/<image-name>
```















