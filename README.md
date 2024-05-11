# Services

### Aplication: 8000
- explore Albion Online items and recipes.  
- login requiered to set:
  - average price for items
  - crafting station use tax

### Mongo-Express: 8001
Direct access to DB.

### Grafana: 8002
Monitor Nginx gateway and system CPU usage.




# Deployment options:

### stack.yml
static swarm deployment


### docker-compose.yml
local deployment  
(for dev)

### portainer/
static portainer (local/swarm)  
usable for github CI/CD swarm deployments
