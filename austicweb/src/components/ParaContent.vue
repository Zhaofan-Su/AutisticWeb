<template>
  <v-timeline align-top>
    <v-timeline-item
      v-for="(content,index) in contents"
      :key="index"
      :color="items[index].color"
      :icon="items[index].icon"
    >
      <v-card :color="items[index].color" dark>
        <v-card-title class="title"></v-card-title>
        <v-card-text class="white text--primary">
          <p class="content">{{content.content}}</p>
        </v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
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
      items: [
        {
          color: 'red lighten-2',
          icon: 'mdi-home'
        },
        {
          color: 'purple darken-1',
          icon: 'mdi-book-variant'
        },
        {
          color: 'green lighten-1',
          icon: 'mdi-gavel'
        },
        {
          color: 'indigo',
          icon: 'mdi-buffer'
        },
        {
          color: 'cyan',
          icon: 'mdi-book'
        },
        {
          color: 'green lighten-1',
          icon: 'mdi-email'
        },
        {
          color: 'indigo darken-2',
          icon: 'mdi-star'
        },
        {
          color: 'amber lighten-1',
          icon: 'mdi-anchor'
        },
        {
          color: 'light-green accent-3',
          icon: 'mdi-tennis'
        },
        {
          color: 'teal accent-3',
          icon: 'mdi-widgets'
        }
      ]
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
.v-timeline {
  margin: 5% 0;
  padding-bottom: 5%;
}
</style>
