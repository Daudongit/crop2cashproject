<template>
    <div class="container mt-4">
        <div class="row">
            <div class="col-lg-8 m-auto">
            <card title="Login">
                <form @submit.prevent="login" @keydown="form.onKeydown($event)">
                <!-- Email -->
                <div class="form-group row">
                    <label class="col-md-3 col-form-label text-md-right">Email</label>
                    <div class="col-md-7">
                        <input v-model="form.email" 
                            :class="{ 'is-invalid': form.errors.has('email') }" 
                            class="form-control" type="email" name="email" required>
                            <has-error :form="form" field="email" />
                    </div>
                </div>

                <!-- Password -->
                <div class="form-group row">
                    <label class="col-md-3 col-form-label text-md-right">Password</label>
                    <div class="col-md-7">
                        <input v-model="form.password" 
                            :class="{ 'is-invalid': form.errors.has('password') }" 
                            class="form-control" type="password" name="password" required>
                            <has-error :form="form" field="password" />
                    </div>
                </div>

                <!-- Registration link  -->
                <div class="form-group row">
                    <div class="col-md-3" />
                        <div class="col-md-7 d-flex">
                            <router-link :to="{ name: 'signup' }" 
                                class=" ml-auto my-auto">
                                SignUp
                            </router-link>
                        </div>
                </div>

                <div class="form-group row">
                    <div class="col-md-7 offset-md-3 d-flex">
                        <!-- Submit Button -->
                        <v-button :loading="form.busy">
                            Login
                        </v-button>
                    </div>
                </div>
                </form>
            </card>
            </div>
        </div>
    </div>
</template>

<script>
import Form from 'vform'
import Cookies from 'js-cookie'

export default {
  name:'Login',
  middleware: 'guest',

  components: {Form},

  data: () => ({
    form: new Form({
      email: '',
      password: ''
    }),
    remember:true
  }),

  methods: {
    async login () {
      // try submit the form.
        try {
            const { data } = await this.form.post('/api/login')
            if(data.success){
                Cookies.set(
                    'token', data.data.token, 
                    { expires: this.remember ? 365 : null }
                )
                sessionStorage.setItem('email',data.data.email)
            }
        } catch (error) {
           console.log(error)
        }
        // Redirect home.
        this.$router.push({ name: 'dashboard' })
    }
  }
}
</script>
