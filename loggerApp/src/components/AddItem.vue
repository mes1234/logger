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
                  <form
                    class="form-group"
                    @submit.prevent="NewItemAdd([NewItemName,NewItemDescription,NewItemDate])"
                  >
                    <input type="text" name="name" class="form-control" v-model="NewItemName">
                    <input
                      type="text"
                      name="description"
                      class="form-control"
                      v-model="NewItemDescription"
                    >
                    <input
                      type="datetime-local"
                      name="date"
                      v-model="NewItemDate"
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
      NewItemName: "name",
      NewItemDescription: "desc",
      NewItemDate: ""
      //
    };
  },
  mounted() {
    this.NewItemDate = this.$store.getters.GetCurrentDate;
  },
  methods: {
    ...mapActions([
      "GetCurrentDate",
      "NewItemAdd"
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