#FROM ubuntu:latest

#RUN apt-get update && apt-get install -y \
  #  python3.12 \
 #   python3-pip \
  #  python3-venv \  
#    git 

#RUN python3 -m venv /venv
#RUN /venv/bin/pip install PyYAML

#COPY feed.py /usr/bin/feed.py
#COPY entrypoint.sh /entrypoint.sh

#ENTRYPOINT ["/entrypoint.sh"]

FROM ubuntu:latest

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install PyYAML using pip inside a virtual environment
RUN python3 -m venv /venv && /venv/bin/pip install PyYAML

# Copy scripts
COPY feed.py /usr/bin/feed.py
COPY entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]
