# Script to automatically set up a new Prisma project for testing purposes, using the steps in the Getting Started guides.
# Usage: ./setup-project.sh <path-to-directory>
# where <path-to-directory> is the path to the new directory you want the project to be created in

filepath="$1"

mkdir "$filepath"
cd "$filepath"

# Install Prisma and dependencies
npm init -y
npm install prisma typescript ts-node @types/node --save-dev

cat <<EOT >> tsconfig.json
{
  "compilerOptions": {
    "sourceMap": true,
    "outDir": "dist",
    "strict": true,
    "lib": ["esnext"],
    "esModuleInterop": true
  }
}
EOT

# Initiate Prisma (this creates the schema.prisma and .env files)
# You will need to manually add your connection string to the .env file
npx prisma init

# Install the client (this generates it too)
npm install @prisma/client

cat <<EOT >> index.ts
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  // ... you will write your Prisma Client queries here
}

main()
  .then(async () => {
    await prisma.\$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    await prisma.\$disconnect()
    process.exit(1)
  })
EOT
