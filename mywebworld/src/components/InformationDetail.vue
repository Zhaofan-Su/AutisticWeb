<template>
  <div class="main">
    <div class="board">
      <h1 class="title">{{name}}</h1>
      <p class="line">——</p>
      <p class="intro">{{intro}}</p>
    </div>

    <div class="detail">
      <paracontent v-bind:contents="contents"></paracontent>

      <div v-if="subtitles.length > 0">
        <div v-for="subtitle in subtitles" :key="subtitle.id">
          <div class="sub_title">{{subtitle.title}}</div>
          <paracontent v-bind:contents="subtitle.contents"></paracontent>
        </div>
      </div>
      <div v-if="listtitles.length > 0" class="list">
        <div v-for="listtitle in listtitles" :key="listtitle.id">
          <p class="list_title">{{listtitle.title}}</p>
          <listcontent v-bind:contents="listtitle.contents"></listcontent>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ParaContent from './ParaContent'
import ListContent from './ListContent'
export default {
  name: 'InformationDetail',
  data () {
    return {
      id: '',
      name: '',
      intro: '',
      contents: [],
      subtitles: [],
      listtitles: []
    }
  },
  components: {
    'paracontent': ParaContent,
    'listcontent': ListContent
  },
  created () {
    this.getInformationDetail()
  },
  methods: {
    getInformationDetail () {
      this.$http.get(`/information/detail/${this.$route.params.id}`)
        .then(response => {
          console.log(response.data)
          this.name = response.data.name
          this.intro = response.data.intro
          this.contents = response.data.contents
          this.subtitles = response.data.sub_titles
          this.listtitles = response.data.list_titles
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style scoped>
.detail {
  padding-top: 20px;
  padding-bottom: 5%;
  width: 80%;
  height: 100%;
  overflow: hidden;
  margin: 0px auto;
}
.line {
  font-size: 20px;
  font-weight: bold;
}
.board {
  width: 100%;
  background-color: #8256c1;
  color: #ffffff;
  text-align: center;
  padding: 4% 0px;
}
.sub_title,
.list_title {
  color: #8256c1;
  font-weight: bold;
  margin-top: 2%;
}
.list {
  border-top: 1px lightgray solid;
  padding: 2% 0px;
}
</style>
