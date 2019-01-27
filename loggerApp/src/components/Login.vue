<template>
  <div id="login">
    <div class="container login-page">
      <div class="card-extended">
        <div class="card-body">
          <div class="card-title-extended text-center">
            <h3>Login</h3>
          </div>
          <div class="card-text">
            <div class="container">
              <div class="row">
                <div class="col-sm">
                  <form class="form-group" @submit.prevent="tryLogin([username,password])">
                    <input
                      type="text"
                      name="user"
                      placeholder="Username"
                      class="form-control"
                      v-model="username"
                    >
                    <input
                      type="password"
                      name="pass"
                      placeholder="Password"
                      class="form-control"
                      v-model="password"
                    >
                    <input type="submit" name="login" value="Login" class="form-control">
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { mapActions } from "vuex";
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    ...mapActions([
      "tryLogin" //try to login to app
    ])
  }
};
</script>

<style lang= 'scss' scoped>
@import "./src/scss/custom";
</style>