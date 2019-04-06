<template>
  <div class="wrap-banner">
    <div class="main-title">
      <h1>绘梦星空</h1>
      <p class="subtitle">阳光中微笑</p>
      <p class="subtitle">星空下祝福</p>
    </div>
    <!--动态粒子背景-->
    <vue-particles
      color="#fecc11"
      :particleOpacity="0.7"
      :particlesNumber="60"
      shapeType="star"
      :particleSize="4"
      linesColor="#5bae23"
      :linesWidth="1"
      :lineLinked="true"
      :lineOpacity="0.4"
      :linesDistance="100"
      :moveSpeed="2"
      :hoverEffect="true"
      hoverMode="grab"
      :clickEffect="true"
      clickMode="push"
      class="lizi"
    ></vue-particles>

    <MainContent></MainContent>
  </div>
</template>

<script>
import MainContent from './MainContent'
export default {
  name: 'HelloWorld',
  data () {
    return {
      items: [
        require('../assets/images/logo.png'),
        require('../assets/images/logo.png')
      ]
    }
  },
  components: {
    MainContent
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wrap-banner {
  font-family: Arial, Helvetica, sans-serif;
  /* height: 100%; */
  overflow: hidden;
}
.main-title {
  text-align: center;
  color: #8256c1;
  position: absolute;
  top: 15%;
  left: 30%;
  z-index: 999;
}
.main-title h1 {
  font-size: 7rem;
  font-family: "Teko", sans-serif;
  text-shadow: 8px 8px #4204bf;
  text-transform: uppercase;
  margin: 0;
  font-weight: 400;
}
.lizi {
  width: 100%;
  height: 100%;
  margin: 0;
  background-image: url("../assets/images/boy.jpg");
  background-size: cover;
  position: relative;
}
.subtitle {
  font-size: 1.7rem;
  margin: 0;
}
</style>
