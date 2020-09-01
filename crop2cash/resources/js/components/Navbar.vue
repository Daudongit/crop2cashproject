<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <router-link :to="{ name:'home'}" class="navbar-brand">
        Jijiclone
      </router-link>

      <button class="navbar-toggler" type="button" 
        data-toggle="collapse" data-target="#navbarToggler" 
        aria-controls="navbarToggler" aria-expanded="false">
        <span class="navbar-toggler-icon" />
      </button>

      <div id="navbarToggler" class="collapse navbar-collapse">
        <ul class="navbar-nav">
          <!-- <locale-dropdown /> -->
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
        </ul>

        <ul class="navbar-nav ml-auto">
          <!-- Authenticated -->
          <li v-if="email" class="nav-item dropdown">
            <a class="nav-link dropdown-toggle text-dark"
               href="#" role="button" data-toggle="dropdown" 
               aria-haspopup="true" aria-expanded="false">
                <!-- <img :src="user.photo_url" class="rounded-circle profile-photo mr-1"> -->
                {{ email }}
            </a>
            <div class="dropdown-menu">
              <router-link :to="{ name: 'login' }" class="dropdown-item pl-3">
                settings
              </router-link>

              <div class="dropdown-divider" />
              <a href="#" class="dropdown-item pl-3" @click.prevent="logout">
                Logout
              </a>
            </div>
          </li>
          <!-- Guest -->
          <template v-else>
            <li class="nav-item">
              <router-link :to="{ name: 'login' }" class="nav-link" active-class="active">
                Login
              </router-link>
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'signup' }" class="nav-link" active-class="active">
                Register
              </router-link>
            </li>
          </template>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import Cookies from 'js-cookie'

export default {

  data: () => ({
    email:null,

  }),

  created(){
    this.email = sessionStorage.getItem('email')
  },
  methods: {
    async logout () {
      // Log out the user.
      Cookies.remove('token')

      // Redirect to login.
      this.$router.push({ name: 'login' })
    }
  }
}
</script>

<style scoped>
.profile-photo {
  width: 2rem;
  height: 2rem;
  margin: -.375rem 0;
}
</style>
