# TODO
```
/agent-app
│
├── /src                    # Source files
│   ├── /config             # Configuration files and settings (e.g., server addresses, ports)
│   │   └── config.py       # General configuration settings
│   ├── /monitoring         # Core logic for system monitoring (using psutil)
│   │   └── monitor.py      # Functions for monitoring system resources (CPU, memory, disk)
│   ├── /grpc               # gRPC-related code
│   │   ├── /protos         # gRPC protocol definition files (e.g., .proto files)
│   │   │   └── monitor.proto
│   │   ├── /server         # gRPC server implementation
│   │   │   └── server.py   # Start gRPC server and handle requests
│   │   └── /client         # gRPC client-side logic (if needed)
│   │       └── client.py   # Logic for sending requests to gRPC server
│   ├── /utils              # Utility functions (e.g., logging, error handling)
│   │   └── logger.py       # Custom logging functions
│   └── main.py             # Main entry point for the agent (starts monitoring and gRPC server)
│
├── /tests                  # Test files
│   ├── /unit               # Unit tests for monitoring and other logic
│   └── /integration        # Integration tests for gRPC and system monitoring
│
├── /logs                   # Log files
│
├── /scripts                # Scripts for deployment, setup, or running the agent
│
├── /docs                   # Documentation for the project
│
├── requirements.txt        # List of dependencies (psutil, grpcio, etc.)
├── .env                    # Environment variables (e.g., server addresses)
└── .gitignore              # Git ignore file
```
