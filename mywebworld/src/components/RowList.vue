<template>
  <div class="rows">
    <el-row>
      <el-col v-for="s in list" :key="s.name">
        <el-card :body-style="{ padding: '0px' }" shadow="hover">
          <img :src="s.imgSrc" class="image">
          <div style="padding: 14px;">
            <span class="title">{{s.name}}</span>
            <div class="bottom clearfix">
              <div class="detail">{{ s.detail }}</div>
              <el-button type="text" class="button">{{s.operation}}</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'RowList',
  props: {
    list: {
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
.rows {
  margin: 0 auto;
  clear: both;
  padding-top: 5%;
  padding-bottom: 5%;
}
.detail {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
  color: #8256c1;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
.rows .el-col {
  width: 24%;
  margin-left: 7%;
}
</style>
