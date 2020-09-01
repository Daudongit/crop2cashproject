<template>
  <div class="row">
    <div class="col-lg-8 m-auto">
      <!--<card v-if="regSuccessful" title="register">
        <div class="alert alert-success" role="alert">
          verify_email_address
        </div>
      </card>-->
      <card  title="Register">
        <form @submit.prevent="register" @keydown="form.onKeydown($event)">
          <!-- First Name -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">First Name</label>
            <div class="col-md-7">
              <input v-model="form.first_name" 
                :class="{ 'is-invalid': form.errors.has('first_name') }" 
                class="form-control" type="text" name="first_name" required>
                <has-error :form="form" field="first_name" />
            </div>
          </div>

          <!-- Last Name -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">Last Name</label>
            <div class="col-md-7">
              <input v-model="form.last_name" 
                :class="{ 'is-invalid': form.errors.has('last_name') }" 
                class="form-control" type="text" name="last_name" required>
                <has-error :form="form" field="last_name" />
            </div>
          </div>

          <!-- State Of Residence -->
          <div class="form-group row">
            <label class="col-md-3 col-form-label text-md-right">State Of Residence</label>
            <div class="col-md-7">
              <input v-model="form.state_of_residence" 
                :class="{ 'is-invalid': form.errors.has('state_of_residence') }" 
                class="form-control" type="text" name="state_of_residence" required>
                <has-error :form="form" field="state_of_residence" />
            </div>
          </div>

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

          <div class="form-group row">
            <div class="col-md-7 offset-md-3 d-flex">
              <!-- Submit Button -->
              <v-button :loading="form.busy">
                register
              </v-button>
            </div>
          </div>
        </form>
      </card>
    </div>
  </div>
</template>

<script>
import Form from 'vform'
import Cookies from 'js-cookie'

export default {
  middleware: 'guest',

  data: () => ({
    form: new Form({
      first_name: '',
      last_name: '',
      state_of_residence: '',
      email: '',
      password: ''
    }),
  }),

  methods: {
    async register () {
      // Register the seller.
      try{
        const { data } = await this.form.post('/api/signup')
        if(data.success){
            Cookies.set(
                'token', data.data.token, 
                { expires:365 }
            )
        }
      } catch(error){
        // console.log(error)
      }

      // Redirect dashboard.
      this.$router.push({ name: 'dashboard' })
    }
  }
}
</script>
