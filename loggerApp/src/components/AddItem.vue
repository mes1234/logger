<template>
  <div id="main">
    <div class="container login-page">
      <div class="card-extended">
        <div class="card-body">
          <div class="card-title-extended text-center">
            <h3>Add Item</h3>
          </div>
          <div class="card-text">
            <div class="container">
              <div class="row">
                <div class="col-sm">
                  <form class="form-group" @submit.prevent="tryLogin([username,password])">
                    <input
                      type="text"
                      name="description"
                      placeholder="Description"
                      class="form-control"
                      v-model="description"
                    >
                    <input
                      type="datetime-local"
                      name="date"
                      v-bind:value="GetCurrentDate"
                      class="form-control"
                    >
                    <input type="submit" name="add" value="add" class="form-control">
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
  data() {
    return {
      description: ""
      //
    };
  },
  mounted() {
    this.$store.dispatch("UpdateCurrentDate"); //fetch list of projects before running
  },
  methods: {
    ...mapActions([
      "UpdateCurrentDate"
      //
    ])
  },
  computed: {
    ...mapGetters([
      "GetCurrentDate"
      //
    ])
  }
};
</script>

<style lang= 'scss' scoped>
@import "./src/scss/custom";
</style>