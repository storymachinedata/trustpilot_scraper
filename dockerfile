FROM python:3.9-slim


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

RUN pip install --upgrade pip

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 80 for the FastAPI application
EXPOSE 80

# Command to run the application using uvicorn
CMD ["uvicorn", "src.API.main:app", "--host", "0.0.0.0", "--port", "80"]