// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
    head: {
      title: 'Charades',
      htmlAttrs: {
        lang: 'en'
      },
      link: [
        {
          rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'
        }
      ]
    }
  },
  runtimeConfig:{
    public: {
      wsUrl: process.env.NUXT_PUBLIC_WS_URL
    }
  },
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxt/ui'],
  css: ['~/assets/css/main.css']
})
