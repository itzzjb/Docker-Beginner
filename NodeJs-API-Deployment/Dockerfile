# From where do you want to take the base image?
# Base images are available on Docker Hub.
# Base image that we choose must have enough of the comonents of OS, networking, and applications 
# that we need to successfully run our application.
FROM node:slim 
# node:slim is a lightweight version of the node image
# You can find these kind of different images on Docker Hub

# Set the working directory in the container
WORKDIR /app

# Copy all the files in the current directory to the working directory in the container
COPY . /app/

# We need to all install the dependencies for our Node.js application in the container that this image runs
# All the dependencies the application needs are listed in the package.json file
# express.js dependency is listed in the package.json file too
RUN npm install 

# Expose the port the app runs on
EXPOSE 3000

# Now we need to run our Node.js application
# We can do this by running the command node ./index.js
CMD node ./index.js 



