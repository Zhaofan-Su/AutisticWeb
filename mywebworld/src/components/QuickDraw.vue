<template>
  <div class="main">
    <canvas id="drawBoard" width="300" height="300"></canvas>
  </div>
</template>

<script>
import {
  fabric
} from 'fabric'
// import * as tf from '@tensorflow/tfjs'
// import * as tfn from '@tensorflow/tfjs-node'
export default {
  name: 'QuickDraw',
  data () {
    return {
      model: null,
      canvas: null, // 还不知道是啥
      symbols: [{}], // 所有的属性
      coords: [],
      mousePressed: false
    }
  },
  created () {
    // this.loadModel()
    this.prepareCanvas()
  },
  mounted () {
    this.prepareCanvas()
  },
  methods: {
    // async  loadModel () {
    //   this.model = await tf.loadGraphModel('https://github.com/zaidalyafeai/zaidalyafeai.github.io/blob/master/sketcher/model2/model.json')
    //   this.model.predict(tf.zeros([1, 28, 28, 1])).print()
    //   this.allowDrawing()
    //   await this.loadSymbols()
    // },
    prepareCanvas () {
      this.canvas = new fabric.Canvas('drawBoard')
      this.canvas.backgroundColor = '#ffffff'
      this.canvas.isDrawingMode = 0
      this.canvas.freeDrawingBrush.Color = 'black'
      this.canvas.freeDrawingBrush.width = 10
      this.canvas.renderAll()
      this.canvas.on('mouse:up', function (e) { this.getFrame(); this.mousePressed = false })
      this.canvas.on('mouse:down', function (e) { this.mousePressed = true })
      this.canvas.on('mouse:move', function (e) { this.recordCoor(e) })
    },
    recordCoor (event) {
      // 记录当前画点的坐标
      var pointer = this.canvas.getPointer(event.e)
      var x = pointer.x
      var y = pointer.y

      if (x >= 0 && y >= 0 && this.mousePressed) {
        this.coords.push(pointer)
      }
    },
    getMinBox () {
      // 得到当前剪切的最好的小边框
      // 暂不明原因，不能用
      // let minX = 0
      // let minY = 0
      // let maxX = 300
      // let maxY = 300

      var coorX = this.coords.map(function (p) { return p.x })
      var coorY = this.coords.map(function (p) { return p.y })

      // 获得已知坐标中的最小的x，y坐标
      var minCoords = {
        x: Math.min.apply(null, coorX),
        y: Math.min.apply(null, coorY)
      }

      // 获得已知坐标中的最大的x，y坐标
      var maxCoords = {
        x: Math.max.apply(null, coorX),
        y: Math.max.apply(null, coorY)
      }

      return {
        min: minCoords,
        max: maxCoords
      }
    },
    findIndicesOfMax (pred, num) {
      // 找到前num个预测的索引
      var result = []
      for (var i = 0; i < pred.length; i++) {
        // 将预测值的索引压入数组
        result.push(i)
        if (result.length > num) {
          // 对预测值数组进行降序
          result.sort(function (a, b) { return pred[a] - pred[b] })
          // 移除数组中最小的那个索引
          result.pop()
        }
      }
      return result
    },
    findTopValues (pred, num) {
      // 找到前num个预测
      var result = []
      var indices = this.findIndicesOfMax(pred, num)
      for (var i = 0; i < num; i++) {
        result.push(pred[indices[i]])
      }
      return result
    },
    getFrame () {
      // 获取canvas的当前帧
      if (this.coords.length >= 2) {
        // 先得到最小的图像边框区域
        // const mbb = this.getMinBox()
        // const dpi = window.devicePixelRatio
        // var imgData = this.canvas.contextContainer.getImageData(mbb.min.x * dpi, mbb.min.y * dpi, (mbb.max.x - mbb.min.x) * dpi, (mbb.max.y - mbb.mix.y) * dpi)
        // 进行预测
        // const pred = this.mode.predict(preprocess(imgData)).dataSync()
        // const indices = this.findIndicesOfMax(pred, 5)
        // const probs = this.findTopValues(pred, 5)
        // const symbols = this.getSymbols(indices)
        // 输出结果
      }
    },
    getSymbols (indices) {
      var result = []
      for (var i = 0; i < indices.length; i++) {
        result[i] = this.symbols[indices[i]]
        return result
      }
    },
    loadSymbols () {
      this.$http.get('model/calss_names.txt')
        .then(response => {
          var list = response.data.split(/\n/)
          this.symbols = []
          for (var i = 0; i < list.length - 1; i++) {
            this.symbols.push(list[i])
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    allowDrawing () {
      // 允许在canvas上绘图

    }
  }
}
</script>

<style scoped>
.main {
  overflow: hidden;
}
#drawBoard {
  border: 1px solid #d1c2d3;
  margin: 5% auto;
}
</style>
