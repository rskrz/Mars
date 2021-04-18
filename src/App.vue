<template lang="pug">
  #app
    NavBar
    router-view
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import NavBar from "@/components/NavBar.vue"

@Component({
  name: "App",
  components: {
    NavBar
  }
})
export default class App extends Vue {}
</script>

<style scoped lang="scss">
// Some SASS code must exist below in order to include all _global SASS code.
@import url("https://fonts.googleapis.com/css2?family=Zen+Dots&display=swap");
#app {
  font-family: "Zen Dots", cursive;
}
</style>
