<template>
  <div id="particles"></div>
</template>

<script>
import particles from 'particles.js'
export default {
  name: 'Background',
  mounted () {
    particlesJS.load('particles', '../../static/particles.json')
    var p = document.getElementById("particles")
    var c = document.children[0]
    c.setAttribute('width', screen.width)
    c.setAttribute('height', screen.height)
    // cxt.fillRect(0, 0, screen.width, screen.height)
  }
}
</script>
<style scoped>
#particles {
  width: 100%;
  height: 100%;
}
</style>
