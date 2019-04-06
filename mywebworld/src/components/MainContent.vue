<template>
  <div class="main">
    <div class="first-row">
      <div class="chat">
        <h2 class="title">嗨！最近怎样？</h2>
        <!-- <p class="subtitle">把你的心事讲给我听吧</p> -->
        <img src="../assets/images/robot.png">
        <el-row>
          <el-button type="primary">和我聊天吧</el-button>
        </el-row>
      </div>
      <div class="sidebar">
        <h2 class="title">近期活动</h2>
        <ul class="events">
          <li v-for="event in events" :key="event.id">
            <el-card shadow="hover" class="event-card">
              <p class="date">{{event.date}}</p>
              <img class="event-img" :src="event.imgSrc">
              <p class="event-intro">{{event.intro}}</p>
            </el-card>
          </li>
        </ul>
      </div>
    </div>

    <div class="games">
      <p class="subtitle">Have fun with us.</p>
      <rowlist v-bind:list="gamelist"></rowlist>
    </div>

    <div class="informations">
      <p class="subtitle">Some information</p>
      <rowlist v-bind:list="infolist"></rowlist>
    </div>

    <div class="stories">
      <p class="subtitle">Life on the Spectrum</p>
      <rowlist v-bind:list="storylist"></rowlist>
    </div>
  </div>
</template>

<script>
import RowList from './RowList'

export default {
  name: 'MainContent',
  components: {
    'rowlist': RowList
  },
  data () {
    return {
      events: [
        {
          id: 1,
          imgSrc: require('../assets/images/logo.png'),
          intro: 'test1',
          date: '2019 3 29 | Shanghai'
        },
        {
          id: 2,
          imgSrc: require('../assets/images/logo.png'),
          intro: 'test2',
          date: '2019 3 29 | Shanghai'
        },
        {
          id: 3,
          imgSrc: require('../assets/images/logo.png'),
          intro: 'test3',
          date: '2019 3 29 | Shanghai'
        }
      ],
      gamelist: [
        {
          name: '你画我猜',
          intro: new Date(),
          imgSrc: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          operation: '开始游戏'
        },
        {
          name: 'game2',
          intro: new Date(),
          imgSrc: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          operation: '开始游戏'
        },
        {
          name: 'game3',
          intro: new Date(),
          imgSrc: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          operation: '开始游戏'
        }
      ],
      infolist: [
        {
          name: '什么是自闭症',
          intro: new Date(),
          imgSrc: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          operation: 'Read More'
        },
        {
          name: 'info2',
          intro: new Date(),
          imgSrc: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          operation: 'Read More'
        },
        {
          name: 'info3',
          intro: new Date(),
          imgSrc: 'https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png',
          operation: 'Read More'
        }
      ],
      storylist: [
        {
          id: 1,
          name: 'LEONARDO | 4 YEARS OLD',
          intro: '“Leo makes everything special. Hace especial todo”, dice Jessica, la mamá de Leo. “ El marca la diferencia entre mis dos hijos. El marca donde quiera que va la diferencia.”',
          imgSrc: require('../assets/images/Leonardo_hero_2.jpg'),
          operation: 'Read More'
        },
        {
          id: 2,
          name: 'BRIDGET L. | 10 YEARS OLD',
          intro: '“Bridget is the pure heart of our family,” says Larry of his 10-year-old daughter.',
          imgSrc: require('../assets/images/Bridget_SMALL_1.jpg'),
          operation: 'Read More'
        },
        {
          id: 3,
          name: 'BRANDON B. | 49 YEARS OLD',
          intro: '“I don’t think he sees the world as a challenge and I don’t see him being challenged by society,” says Reese, Brandon\'s brother.',
          imgSrc: require('../assets/images/Brandon_SMALL_0.jpg'),
          operation: 'Read More'
        }
      ]
    }
  }
}
</script>

<style scoped>
.main {
  padding-top: 20px;
  /* padding-bottom: 5%; */
  width: 80%;
  height: 100%;
  overflow: hidden;
  margin: 0px auto;
  clear: both;
  border-radius: 4px;
  border: 1px lightgrey solid;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.first-row,
.games,
.stories {
  margin: 5% auto;
  overflow: hidden;
}
/* 以下设置左侧聊天块的样式 */
.chat {
  float: left;
  width: 50%;
  padding-left: 7%;
  padding-right: 6%;
}
.title {
  color: #8256c1;
}
.chat img {
  height: 50%;
  width: 50%;
  background-size: cover;
  margin: 5% auto;
}

/* 以下设置右侧活动的样式 */
.sidebar {
  float: right;
  width: 30%;
  padding-right: 7%;
}

.events {
  list-style: none;
  padding-left: 0;
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

.event-card {
  border-right: 0px;
  border-left: 0px;
  border-top: 0px;
}
.games,
.stories {
  background-color: #f2f2f2;
}

.subtitle {
  color: #8256c1;
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  margin-top: 5%;
}
</style>
