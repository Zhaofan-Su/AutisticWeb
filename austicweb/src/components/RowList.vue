<template>
  <div class="rows">
    <el-row>
      <el-col v-for="s in list" :key="s.detail.id">
        <v-hover>
          <v-card
            slot-scope="{ hover }"
            :class="`elevation-${hover ? 12 : 2}`"
            class="md-auto"
            color="grey lighten-4"
          >
            <v-img :src="s.imgSrc">
              <v-expand-transition>
                <div
                  v-if="hover"
                  class="d-flex transition-fast-in-fast-out grey darken-1 v-card--reveal display-3 white--text"
                  style="height:100%"
                ></div>
              </v-expand-transition>
            </v-img>
            <v-card-text class="pt-4" style="position:relative">
              <h3 class="subheading font-weight-bold _title mb-2">{{s.detail.name}}</h3>
              <div class="font-weight-light intro">{{s.detail.intro}}</div>
            </v-card-text>
            <v-card-actions>
              <v-btn flat dark color="#8256c1" @click="goToDetail(s.detail.id)">{{s.operation}}</v-btn>
              <v-spacer></v-spacer>
              <v-btn icon @click="goToDetail(s.detail.id)">
                <v-icon>{{'keyboard_arrow_right'}}</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-hover>
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
    },
    type: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      // show: false
    }
  },
  created () {
  },
  methods: {
    goToDetail (id) {
      this.$router.push(`/${this.type}/${id}`)
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

._title {
  color: #8256c1;
  font-weight: bold;
}
.intro {
  font-size: 13px;
  color: grey;
  display: inline-block;
  line-height: 21px;
  font-weight: 400;
}

.v-card {
  border-radius: 12px;
}
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.5;
  position: absolute;
  width: 100%;
  cursor: pointer;
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
