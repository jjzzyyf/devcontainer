# Use the official Microsoft SQL Server 2022 image
FROM mcr.microsoft.com/mssql/server

# Set the working directory to /workspaces/mssql
WORKDIR /workspaces/mssql

# Copy the backups, data, and logs folders to the container
ADD . /workspaces/mssql

# Download the AdventureWorks2019 database to the backups folder
# RUN curl -o /workspaces/mssql/backup/AdventureWorks2019.bak \
#     https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorks2022.bak

# Expose the SQL Server port
EXPOSE 1433
