<template>
  <div id="App">
    <Navigation></Navigation>
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>

<script>
import Navigation from './components/Navigation'
import Footer from './components/Footer'

export default {
  name: 'App',
  components: {
    Navigation, Footer
  }
}
</script>

<style>
* {
  margin: 0px;
}
#App {
  height: 100%;
}
</style>
