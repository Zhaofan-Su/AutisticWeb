<template>
  <div class="contents">
    <p class="content" v-for="content in contents" :key="content.id">{{content.content}}</p>
  </div>
</template>

<script>
export default {
  name: 'ParaContent',
  props: {
    contents: {
      type: Array,
      required: true
    }
  },
  data () {
    return {

    }
  }
}
</script>

<style scoped>
.content {
  padding: 2%;
  margin: 2px auto;
  font-size: 12px;
  color: #646464;
}
</style>
