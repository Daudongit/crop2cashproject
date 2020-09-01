<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-header">{{ __('Register') }}</div>

          <div class="card-body">
            <form @submit.prevent="onSubmit($event)">
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="inputFirstname4">First name</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="user.firstname"
                    id="inputFirstname4"
                    placeholder="Firstname"
                  />
                </div>
                <div class="form-group col-md-6">
                  <label for="inputLastname4">Last name</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="user.lastname"
                    id="inputLastname4"
                    placeholder="Lastname"
                  />
                </div>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="inputSex">Sex</label>
                  <select id="inputSex" v-model="user.gender" class="form-control">
                    <option selected>Choose...</option>
                    <option>Male</option>
                    <option>Female</option>
                  </select>
                </div>
                <div class="form-group col-md-4">
                  <label for="inputDate">Date of Birth</label>
                  <input type="date" class="form-control" v-model="user.birth" />
                </div>
                <div class="form-group col-md-2">
                  <label for="inputPhone">Phone Number</label>
                  <input type="tel" class="form-control" v-model="user.phone" id="inputPhone" />
                </div>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="inputAddress">Address</label>
                  <input type="text" class="form-control" v-model="user.address" id="inputAddress" />
                </div>
                <div class="form-group col-md-3">
                  <label for="inputArea">Area</label>
                  <input type="text" class="form-control" v-model="user.area" id="inputArea" />
                </div>
                <div class="form-group col-md-3">
                  <label for="inputCity">City/Town</label>
                  <input type="text" class="form-control" v-model="user.city" id="inputCity" />
                </div>
              </div>

              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="inputState">State</label>
                  <input type="text" class="form-control" v-model="user.state" id="inputState" />
                </div>
                <div class="form-group col-md-3">
                  <label for="inputLG">Local Government</label>
                  <input type="text" class="form-control" v-model="user.LG" id="inputLG" />
                </div>
                <div class="form-group col-md-3">
                  <label for="inputCountry">Country</label>
                  <input type="text" class="form-control" v-model="user.country" id="inputCountry" />
                </div>
              </div>
              <div class="form-row">
                <div class="form-group col-md-4">
                  <label for="inputusername">Username</label>
                  <input
                    type="text"
                    class="form-control"
                    v-model="user.username"
                    id="inputusername"
                  />
                </div>
                <div class="form-group col-md-4">
                  <label for="inputPassword">Password</label>
                  <input
                    type="password"
                    class="form-control"
                    v-model="user.password"
                    id="inputPassword"
                  />
                </div>
                <div class="form-group col-md-3">
                  <label for="inputcpassword">Confirm Password</label>
                  <input
                    type="password"
                    class="form-control"
                    v-model="user.cpassword"
                    id="inputcpassword"
                  />
                </div>
              </div>
              <div class="form-group">
                <div class="form-check">
                  <input class="form-check-input" v-model="user.TC" type="checkbox" id="gridCheck" />
                  <label class="form-check-label" for="gridCheck">
                    I have read and agree with the
                    <a href="#">Terms and Conditions</a>
                  </label>
                </div>
              </div>
              <button type="submit" :disabled="create" class="btn btn-primary">Create Accont</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      user: {
        id: null,
        name: "",
        email: ""
      }
    };
  },
  methods: {
    onSubmit(event) {
      this.create = true;

      api
        .update(this.user.id, {
          name: this.user.name,
          email: this.user.email
        })
        .then(response => {
          this.message = "User updated";
          setTimeout(() => (this.message = null), 2000);
          this.user = response.data.data;
        })
        .catch(error => {
          console.log(error);
        })
        .then(_ => (this.create = false));
    }
  },
  created() {
    // @todo load user details
  }
};
</script>
<style scoped>
</style>
