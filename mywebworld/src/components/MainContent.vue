<template>
  <div class="main">
    <div class="chat">
      <h1 class="title">嗨！最近怎样？</h1>
      <p class="subtitle">把你的心事讲给我听吧</p>
      <img src="../assets/robot.jpg">
      <el-row>
        <el-button type="primary">和我聊天吧</el-button>
      </el-row>
    </div>
    <div class="sidebar">
      <ul class="events">
        <li v-for="event in events" :key="event.id">
          <el-card shadow="hover">
            <p class="date">{{event.date}}</p>
            <img class="event-img" src="event.imgSrc">
            <p class="event-detail">{{event.detail}}</p>
          </el-card>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainContent',
  data () {
    return {
      events: [{
        id: 1,
        imgSrc: '../assets/logo.png',
        detail: 'test1',
        date: '2019 3 29 | Shanghai'
      },
      {
        id: 2,
        imgSrc: '../assets/logo.png',
        detail: 'test2',
        date: '2019 3 29 | Shanghai'
      },
      {
        id: 3,
        imgSrc: '../assets/logo.png',
        detail: 'test3',
        date: '2019 3 29 | Shanghai'
      }]
    }
  }
}
</script>

<style scoped>
.main {
  padding-left: 5%;
  padding-right: 5%;
  padding-top: 20px;
  padding-bottom: 5%;
  width: 80%;
  height: 100%;
  overflow: hidden;
  margin-left: 10%;
  margin-right: 10%;
  clear: both;
  border-radius: 4px;
  border: 1px lightgrey solid;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.chat {
  float: left;
  width: 60%;
  padding-left: 2px;
  padding-right: 6%;
}
.title {
  color: #8256c1;
}
.chat img {
  height: 50%;
  width: 50%;
  background-size: cover;
}
.sidebar {
  float: right;
  width: 30%;
  padding-right: 2%;
}
.events {
  list-style: none;
}
.event-img {
  width: 50px;
  height: 50px;
  background-size: cover;
  float: left;
}

.el-button--primary {
  background-color: #8256c1;
  border-color: #8256c1;
}

.el-card {
  border-right: 0px;
  border-left: 0px;
}
</style>
