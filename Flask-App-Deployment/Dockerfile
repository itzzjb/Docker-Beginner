# Dockerfile is a text file that contains instructions for building a Docker image.

# Always start with a base image
FROM python:3-alpine3.16 
#alpine means it is a lightweight version of the image

# Set the working directory in the container (This is like a folder in the container when it acts like a OS)
WORKDIR /app

# Copy the dependencies file to the working directory
# We move all of our files to the working directory
COPY . /app/

# Install dependencies (that in the requirements.txt file)
# We can run any command that we can run in the terminal here.
# So, we can use commands to install dependencies here.
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 3000

# Run the application
# This is the command that will run when the container starts.
CMD python ./index.py

