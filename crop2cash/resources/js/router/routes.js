import Login from '../pages/auth/Login.vue'
import Register from '../pages/auth/Register.vue'
import Home from '../pages/Home.vue'
import Dashboard from '../pages/Dashboard.vue'

export default [
  // { path: '/', name: 'login', component: Login, meta:{layout:LoginLayout} },
  { path: '/', name: 'home', component: Home },
  { path: '/login', name: 'login', component: Login },
  { path: '/signup', name: 'signup', component: Register },
  { path: '/dashboard', name: 'dashboard', component: Dashboard},  
    // { path: '*', component: page('errors/404.vue') }
]