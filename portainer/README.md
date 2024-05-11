Used for deployment using potainer

Instructions
1. Start potainer container (compose up -d in here)
2. Connection through https to portainer: portainer initial setup (password)...
3. Through portainer GUI: Stacks > Add stack
 - Name: ****
 - Build method: Repository
 - repo url: https://github.com/CristiSima/IDP
 - compose path: stack.yml
 - GitOps updates: y
4. Deploy stack