<template>
  <div id="calc">
    <div class="container">
      <div class="card-extended">
        <div class="card-body">
          <div class="card-title-extended text-center">
            <h3>Logger App</h3>
          </div>
          <div class="card-text">
            <div class="container">
              <div class="row">
                <div class="col-sm">
                  <project-select></project-select>
                  <add-item></add-item>
                  <show-items></show-items>
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
import ProjectSelect from "./ProjectSelect.vue";
import AddItem from "./AddItem.vue";
import ShowItems from "./ShowItems.vue";
export default {
  name: "app",
  components: {
    "project-select": ProjectSelect,
    "add-item": AddItem,
    "show-items": ShowItems
  }
};
</script>

<style lang= "scss" scoped>
@import "./src/scss/custom";
</style>