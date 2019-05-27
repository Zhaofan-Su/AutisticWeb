<template>
  <!-- <div id="App">
    <Navigation></Navigation>
  <router-view></router-view>-->
  <!-- <Live2d></Live2d> -->
  <!-- <Footer></Footer>
  </div>-->
  <div id="App">
    <Navigation></Navigation>
    <router-view></router-view>

    <Footer></Footer>
  </div>
</template>

<script>
import Navigation from './components/Navigation'
import Footer from './components/Footer'
import Live2d from './components/Live2d'

export default {
  name: 'App',
  components: {
    Navigation, Footer, Live2d
  }

}
</script>

<style>
* {
  margin: 0px;
}
#App {
  height: 100%;
  background-color: #fdf4eb;
}
/* .el-radio__input.is-checked .el-radio__inner {
  background-color: #8256c1;
  border-color: #8256c1;
}
.el-radio__input.is-checked + .el-radio__label {
  color: #8256c1;
} */
</style>
