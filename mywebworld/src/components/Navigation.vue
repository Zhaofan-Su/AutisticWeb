<template>
  <div class="nav">
    <div class="image"></div>
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      text-color="#8256c1"
      active-text-color="#4204bf"
      @select="handleSelect"
    >
      <el-menu-item index="4">加入我们</el-menu-item>
      <el-menu-item index="3">轻松一刻</el-menu-item>
      <el-menu-item index="2">帮助和建议</el-menu-item>
      <el-menu-item index="1">关于</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'Navigation',
  data () {
    return {
      activeIndex: '1'
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>
.nav {
  position: absolute;
  z-index: 999;
  width: 100%;
}
.el-menu-demo li {
  float: right;
}
.image {
  width: 20px;
  height: 20px;
  background-color: brown;
  float: left;
  position: absolute;
  z-index: 1000;
}
</style>
