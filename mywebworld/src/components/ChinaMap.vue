<template>
  <div class="echarts">
    <div id="mapChart" :style="{height:'500px',width:'100%'}" ref="myEchart"></div>
    <div class="back">
      <el-button icon="el-icon-arrow-left" @click="back">上一页</el-button>
    </div>
  </div>
</template>

<script>
import cityMap from '../js/china-main-city-map.js'


// 中国地图（第一级地图）的ID、Name、Json数据
var chinaId = 100000
var chinaName = 'china'
var chinaJson = null

// 记录父级ID、Name
var mapStack = []
var parentId = null
var parentName = null

// Echarts地图全局变量，在返回上级地图的方法中会用到
var myChart = null
var echarts = null
var axios = null
var data = []
export default {
  name: 'ChinaMap',
  data () {
    return {
      chart: null,
      schools: []
    }
  },
  created () {
    echarts = this.$echarts
    axios = this.$http
  },
  mounted () {
    this.mapChart('mapChart')
  },
  beforeDestroy () {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    back () {
      if (mapStack.length != 0) {
        // 如果有上级目录则执行
        var map = mapStack.pop()
        axios.get('http://localhost:8081/static/map/' + map.mapId + '.json', {})
          .then(response => {
            const mapJson = response.data
            registerAndsetOption(
              myChart,
              map.mapId,
              map.mapName,
              mapJson,
              false
            )
            // 返回上一级后，父级的ID、Name随之改变
            parentId = map.mapId
            parentName = map.mapName
          })
      }
    },
    // Echarts地图
    mapChart (divId) {
      axios.get('http://localhost:8081/static/map/' + chinaId + '.json', {})
        .then(response => {
          const mapJson = response.data
          chinaJson = mapJson
          myChart = this.$echarts.init(document.getElementById(divId))
          registerAndsetOption(myChart, chinaId, chinaName, mapJson, false)
          parentId = chinaId
          parentName = 'china'
          myChart.on('click', function (param) {
            var cityId = cityMap[param.name]
            if (cityId) {
              // 代表有下级地图
              axios.get('http://localhost:8081/static/map/' + cityId + '.json', {})
                .then(response => {
                  const mapJson = response.data
                  registerAndsetOption(
                    myChart,
                    cityId,
                    param.name,
                    mapJson,
                    true
                  )
                })
            } else {
              // 没有下级地图，回到一级中国地图，并将mapStack清空
              registerAndsetOption(myChart, chinaId, chinaName, chinaJson, false)
              mapStack = []
              parentId = chinaId
              parentName = chinaName
            }
          })
        })
    }
  }
}
/**
 *
 * @param {*} myChart
 * @param {*} id        省市县Id
 * @param {*} name      省市县名称
 * @param {*} mapJson   地图Json数据
 * @param {*} flag      是否往mapStack里添加parentId，parentName
 */
function registerAndsetOption (myChart, id, name, mapJson, flag) {
  echarts.registerMap(name, mapJson)
  var path = ''
  if (name == 'china') {
    path = `school/province`
  }
  else {
    path = `school/${name}/city`
  }
  axios.get(path)
    .then(response => {
      var provinces = []
      var nums = []
      var mapData = []
      var myData = []
      response.data.forEach(ele => {
        if (ele['province']) {
          provinces.push(ele['province'])
          myData.push({
            name: ele['province'],
            value: ele['count']
          })
          nums.push(ele['count'])
        }
        else if (ele['city']) {
          provinces.push(ele['city'])
          myData.push({
            name: ele['city'],
            value: ele['count']
          })
          nums.push(ele['count'])
        }

      })
      mapData = initMapData(mapJson, provinces, nums)
      myChart.setOption({
        tooltip: {
          // formatter: function (a) {
          //   return ('自闭症康复机构数目'
          //     + '</br>' + a['name'] + ':\t\t' + a['value'][2] + '家')
          // },
        },
        geo: {
          map: name,
          roam: true,
          zoom: 1.2,
          label: {
            normal: {
              show: false,
              textStyle: {
                color: 'rgba(0,0,0,0.4)'
              }
            }
          },
          data: mapData,
          itemStyle: {
            normal: {
              areaColor: 'rgba(23, 27, 57,0)',
              borderColor: '#813c85',
              borderWidth: 1
            },
            emphasis: {
              shadowBlur: 20,
              shadowColor: 'rgba(0,0,0,0.5)',
              areaColor: '#d1c2d3'
            }
          }
        },
        series: [
          {
            name: '自闭症康复机构数目Top5',
            type: 'effectScatter',
            coordinateSystem: 'geo',
            data: mapData.sort(
              function (a, b) {
                return b.value[2] - a.value[2]
              }
            ).slice(0, 6),
            symbolSize: function (val) {
              return val[2] * 6 / 5;
            },
            tooltip: {
              formatter: function (a) {
                return ('自闭症康复机构数目Top5'
                  + '</br>' + a['name'] + ':\t\t' + a['value'][2] + '家')
              },
            },
            showEffectOn: 'emphasis',
            rippleEffect: {
              brushType: 'stroke'
            },
            hoverAnimation: true,
            label: {
              normal: {
                formatter: '{b}',
                position: 'right',
                show: true
              },
              emphasis: {
                show: true
              }
            },
            itemStyle: {
              normal: {
                color: '#f4e925',
                shadowBlur: 10,
                shadowColor: '#333'
              }
            }
          },
        ]
      })
      if (flag) {
        // 往mapStack里添加parentId，parentName,返回上一级使用
        mapStack.push({
          mapId: parentId,
          mapName: parentName
        })
        parentId = id
        parentName = name
      }
    })
}

function initMapData (mapJson, provinces, nums) {
  var mapData = []

  for (var i = 0; i < mapJson.features.length; i++) {
    if (provinces.length != 0) {
      var name = mapJson.features[i].properties.name
      var num = provinces.indexOf(name) != -1 ? nums[provinces.indexOf(name)] : 0
      mapData.push({
        name: name,
        value: mapJson.features[i].properties.cp.concat(num)
      })
    }
  }
  return mapData
}
</script>
<style scoped>
.echarts {
  margin-top: 5%;
}
.back {
  margin: 2% 50% 5% 50%;
}
</style>
