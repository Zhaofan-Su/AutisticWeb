<template>
  <div class="list">
    <ul>
      <li v-for="content in contents" :key="content.id" class="content">{{content.content}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ListContent',
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
  padding: 1% 0;
  margin: 2px auto;
  font-size: 12px;
  color: #646464;
}
</style>
