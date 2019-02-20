<template>
  <div id="main">
    <div class="container login-page">
      <div class="card-extended">
        <div class="card-body">
          <div class="card-title-extended text-center">
            <h3>Show Item</h3>
          </div>
          <div class="card-text">
            <div class="container">
              <div class="row">
                <div class="col-sm">
                  <ol>
                    <li
                      v-for="item in GetItems"
                      :key="item.id"
                      :value="item.id"
                    >{{item.description}}:{{item.date}}</li>
                  </ol>
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
      //
    };
  },
  methods: {
    ...mapActions([
      //
    ])
  },
  computed: {
    ...mapGetters([
      "GetItems"
      //
    ])
  }
};
</script>

<style lang= 'scss' scoped>
@import "./src/scss/custom";
</style>