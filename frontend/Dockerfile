
FROM node:22-alpine AS build
WORKDIR /nuxt

RUN corepack enable

COPY package.json pnpm-lock.yaml .npmrc ./

RUN pnpm i

COPY . ./

RUN pnpm run build

FROM node:22-alpine
WORKDIR /nuxt

COPY --from=build /nuxt/.outpit/ ./

ENV PORT=3000
ENV HOST=0.0.0.0

EXPOSE 3000

# FOR DEV
#CMD ["npm run dev"]

# FOR BUILD
CMD ["node", "/nuxt/server/index.mjs"]