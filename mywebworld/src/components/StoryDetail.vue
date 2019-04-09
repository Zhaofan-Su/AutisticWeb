<template>
  <div class="main">
    <div class="board">
      <h1>
        认识
        <span class="title">{{name}}</span>
      </h1>
    </div>
    <div class="detail">
      <div class="subtitle">
        <h2>{{name}} | {{age}}</h2>
      </div>

      <div class="intro">
        <p class="quote">&quot;</p>
        {{intro}}
      </div>

      <div class="contents">
        <p class="content" v-for="content in contents" :key="content">{{content.content}}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StoryDetail',
  props: {

  },
  data () {
    return {
      id: '',
      name: 'LEONARDO ',
      age: '4 Years old',
      intro: 'Leo makes everything special. Hace especial todo”, dice Jessica, la mamá de Leo. “ El marca la diferencia entre mis dos hijos. El marca donde quiera que va la diferencia.',
      contents: [
        {
          content: 'test1'
        },
        {
          content: 'test1'
        },
        {
          content: 'test1'
        }
      ]
    }
  },
  created () {
    this.getStoryDetail(this.$route.params.id)

    this.id = this.$route.params.id
    console.log(this.id)
  },
  methods: {
    getStoryDetail (id) {
      this.$http.get(`/story/detail/${id}`)
        .then(response => {
          console.log(response.data)
        })
    }
  }
}
</script>

<style scoped>
.subtitle,
.intro {
  padding: 2%;
  border-bottom: 1px lightgray solid;
}
.board {
  width: 100%;
  background-color: #8256c1;
  text-align: center;
  color: #ffffff;
  padding: 4% 4%;
}
.title {
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

.content {
  padding: 2%;
  margin: 2px auto;
  font-size: 12px;
  color: #646464;
}
</style>
