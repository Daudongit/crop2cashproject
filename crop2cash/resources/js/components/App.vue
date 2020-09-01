<template>
  <div id="app">
    <router-view />
      <!-- <component :is="this.$route.meta.layout || 'div'">
          <router-view />
      </component> -->
      <!-- <component :is="layout">
          <router-view :layout.sync="layout"/>
      </component> -->
  </div>
</template>

<script>
import DefaultLayout from '../layouts/DefaultLayout.vue'

export default {
    el: '#app',
    name:'App',

    data: () => ({
        // layout: null,
        // layout: DefaultLayout,
    }),
    methods:{
      setLayout (layout) {
         this.layout = DefaultLayout
      }
    }
}
</script>
