<template lang="pug">
  #NavBar.flex.justify-between.mh4.items-center
    h1 Life On Mars?
    .flex
      a.white.f2.mr4 Home
      a.white.f2.mr4 About
      a.white.f2 Contact
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
@Component({
  name: "NavBar"
})
export default class NavBar extends Vue {}
</script>

<style lang="scss" scoped>
#NavBar {
}
</style>
