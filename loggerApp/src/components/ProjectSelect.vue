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
                  <form>
                    <select
                      v-model="projectSelected"
                      name="project"
                      @change="setCurrentProjectId({projectSelected})"
                      class="form-control form-control-sm"
                    >
                      <option
                        v-for="project in ListProjects"
                        :key="project.id"
                        :value="project.id"
                      >{{project.description}}</option>
                    </select>
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
      projectSelected: 0
    };
  },
  mounted() {
    this.$store.dispatch("getListOfProjects"); //fetch list of projects before running
  },
  methods: {
    ...mapActions([
      "setCurrentProjectId" //update store id of currently used project
    ])
  },
  computed: {
    ...mapGetters([
      "ListProjects" //return all project
    ])
  }
};
</script>

<style lang= 'scss' scoped>
@import "./src/scss/custom";
</style>