<template>
  <div class="main">
    <div class="board">
      <h1 class="title">
        认识
        <span class="name">{{name}}</span>
      </h1>
    </div>
    <div class="detail">
      <div class="subtitle">
        <h2>{{name}} | {{age}} years old</h2>
      </div>

      <div class="intro">
        <p class="quote">&quot;</p>
        {{intro}}
      </div>

      <div class="embed-youtube">
        <iframe
          width="100%"
          height="480"
          frameborder="0"
          allowfullscreen="allowfullscreen"
          :src="videoUrl"
          v-loading="loading"
          element-loading-text="拼命加载中"
          element-loading-spinner="el-icon-loading"
          element-loading-background="rgba(0, 0, 0, 0.8)"
          @onload="load"
        ></iframe>
      </div>
      <paraContent v-bind:contents="contents"></paraContent>
    </div>
  </div>
</template>

<script>
import ParaContent from './ParaContent'
export default {
  name: 'StoryDetail',
  data () {
    return {
      id: '',
      name: '',
      age: '',
      intro: '',
      videoUrl: '',
      contents: [],
      loading: true
    }
  },
  components: {
    'paraContent': ParaContent
  },
  created () {
    this.getStoryDetail()
  },
  methods: {
    getStoryDetail () {
      this.$http.get(`/story/detail/${this.$route.params.id}`)
        .then(response => {
          this.age = response.data.age
          this.name = response.data.name
          this.intro = response.data.intro
          this.videoUrl = response.data.videoUrl
          this.contents = response.data.contents
        })
        .catch(error => {
          console.log(error)
        })
    },
    load () {
      this.loading = false
    }
  }
}
</script>

<style scoped>
.subtitle,
.intro {
  padding: 2% 0px;
  border-bottom: 1px lightgray solid;
}
.board {
  width: 100%;
  background-color: #8256c1;
  text-align: center;
  color: #ffffff;
  padding: 4% 0px;
}
.name {
  margin: 0 3%;
}
.detail {
  padding-top: 20px;
  /* padding-bottom: 5%; */
  width: 80%;
  height: 100%;
  overflow: hidden;
  margin: 0px auto;
}
.subtitle {
  color: #8256c1;
  padding-left: 0;
}
.quote {
  color: #8256c1;
  display: inline-block;
  font-size: 40px;
}
.embed-youtube {
  margin: 2% auto;
  width: 80%;
}
</style>
