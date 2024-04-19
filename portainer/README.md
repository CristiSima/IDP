Used for deployment using potainer

Instructions
1. Start potainer container (compose up -d in here)
2.  ... potainer initial setup ...
3. Stacks > Add stack
 - Name: ****
 - Build method: Repository
 - repo url: https://github.com/CristiSima/IDP
 - compose path: stack.yml
 - GitOps updates: y
4. Deploy stack