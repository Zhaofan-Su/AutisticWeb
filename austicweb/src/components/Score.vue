<template>
  <div>
    <div id="intro" v-if="!test">
      <div class="text-xs-center">
        <v-dialog v-model="dialog" width="500">
          <v-card>
            <v-card-title class="headline deep-purple lighten-1" primary-title></v-card-title>
            <v-card-text>本测评是儿童孤独症评定量表（childhood autism rating scale 简称CARS量表），孤独症也叫自闭症，该量表编制于２０世纪８０年代初，从１５个主要方面对孤独症儿童进行评估，是主要适用于专业人员评定（如医师或儿童心理测验专职人员），应用时最好能结合儿童孤独症家长评定量表共同使用。</v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
              <v-spacer>
                <v-btn color="#8256c1" round @click="dialog = false" style="color:#fff">进入测试</v-btn>
              </v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
      <!-- <p>本测评是儿童孤独症评定量表（childhood autism rating scale 简称CARS量表），孤独症也叫自闭症，该量表编制于２０世纪８０年代初，从１５个主要方面对孤独症儿童进行评估，是主要适用于专业人员评定（如医师或儿童心理测验专职人员），应用时最好能结合儿童孤独症家长评定量表共同使用。</p> -->
      <!-- <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>测试须知</span>
        </div>
        <div class="item">
          <span class="note">题目数</span>
          <span class="note-description">15题</span>
        </div>
        <div class="item">
          <span class="note">预计用时</span>
          <span class="note-description">约15分钟</span>
        </div>
        <div id="start">
          <el-button type="primary" round v-on:click="startTest">开始测试</el-button>
        </div>
      </el-card>-->
    </div>
    <div class="empty" v-if="dialog"></div>
    <div v-else>
      <div class="progress">
        <el-progress :percentage="parseInt(((active+1)/15)*100)" color="#8e71c7"></el-progress>
      </div>
      <div id="question">
        <el-card class="box-card" v-if="questions.length!=0">
          <div slot="header" class="clearfix">
            <span>{{questions[active].title}}</span>
          </div>
          <el-radio-group class="option" v-model="checkedValue">
            <p class="text item">
              <el-radio :label="1">{{questions[active].proper}}</el-radio>
            </p>
            <p class="text item">
              <el-radio :label="2">{{questions[active].mild}}</el-radio>
            </p>
            <p class="text item">
              <el-radio :label="3">{{questions[active].moderate}}</el-radio>
            </p>
            <p class="text item">
              <el-radio :label="4">{{questions[active].badly}}</el-radio>
            </p>
          </el-radio-group>
        </el-card>
      </div>
      <div class="button" v-if="active!=14">
        <el-button type="primary" icon="el-icon-arrow-left" v-on:click="lastQuestion">上一题</el-button>
        <el-button type="primary" v-on:click="nextQuestion">
          下一题
          <i class="el-icon-arrow-right el-icon--right"></i>
        </el-button>
      </div>
      <div class="button" v-else>
        <el-button type="primary" icon="el-icon-arrow-left" v-on:click="lastQuestion">上一题</el-button>
        <el-button type="primary" v-on:click="finish">
          完&nbsp;&nbsp;成
          <i class="el-icon-check el-icon--right"></i>
        </el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Score',
  data () {
    return {
      dialog: true,
      labelPosition: 'top',
      test: false,
      questions: [],
      active: 0,
      checkedValue: 0,
      sum: 0,
      choices: []
    }
  },
  created () {
    this.getQuestions()
  },
  methods: {
    getQuestions () {
      this.$http.get(`question/all`)
        .then(response => {
          response.data.forEach(element => {
            let question = {}
            question.title = element.title
            question.proper = element.proper
            question.mild = element.mild
            question.moderate = element.moderate
            question.badly = element.badly
            this.questions.push(question)
          })
        })
        .catch(err => {
          console.log(err)
        })
    },
    startTest () {
      this.test = true
    },
    lastQuestion () {
      if (this.active > 0) {
        this.active--
      }
      this.sum -= this.choices[this.active]
      this.checkedValue = this.choices[this.active]
    },
    nextQuestion () {
      this.sum += this.checkedValue
      this.choices[this.active - 1] = this.checkedValue
      if (this.choices[this.active] != null) {
        this.checkedValue = this.choices[this.active]
      }
      else {
        this.checkedValue = 0
      }
      if (this.active < this.questions.length - 1) {
        this.active++
      }
    },
    finish () {

    }
  }
}
</script>

<style scoped>
.item {
  margin-bottom: 18px;
  overflow: hidden;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}
.note,
.note-description {
  color: #646464;
}
.note-description {
  float: right;
}
.box-card {
  width: 50%;
  margin: 5% auto;
}
.empty {
  min-height: 500px;
  height: 100%;
}
.progress {
  width: 55%;
  margin-left: 23%;
}
#start {
  margin-top: 40px;
  text-align: center;
}
#start .el-button,
.button .el-button {
  background-color: #8256c1;
  border: #8256c1;
}
#start .el-button:hover,
.button .el-button:hover {
  background-color: #813c85;
  border: #813c85;
}
#question /deep/ .el-radio__input.is-checked .el-radio__inner {
  background-color: #8256c1;
  border-color: #8256c1;
}
#question /deep/ .el-radio__input.is-checked + .el-radio__label {
  color: #8256c1;
}
.button,
.progress {
  text-align: center;
  margin-bottom: 5%;
  margin-top: 5%;
}
.button /deep/ .el-button + .el-button {
  margin-left: 5px;
}
</style>
