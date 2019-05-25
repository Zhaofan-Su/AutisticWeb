<template>
  <canvas id="drawBoard" width="300" height="300"></canvas>
</template>

<script>
import {
  fabric
} from 'fabric'
import * as tf from '@tensorflow/tfjs'
import { getNumChannels } from '@tensorflow/tfjs-core/dist/backends/webgl/webgl_util';

var model = null
var canvas = null
var symbols = [{}]
var coords = []
var mousePressed = false
export default {
  name: 'QuickDraw',
  data () {
    return {
    }
  },
  created () {
    this.loadModel()
    this.prepareCanvas()
  },
  mounted () {
    this.prepareCanvas()
  },
  methods: {
    async  loadModel () {
      model = await tf.loadLayersModel('../../static/models/model.json')
      model.predict(tf.zeros([1, 28, 28, 1])).print()
      allowDrawing()
      await this.loadSymbols()
    },
    prepareCanvas () {
      canvas = new fabric.Canvas('drawBoard')
      canvas.backgroundColor = '#ffffff'
      canvas.isDrawingMode = 0
      canvas.freeDrawingBrush.Color = 'black'
      canvas.freeDrawingBrush.width = 10
      canvas.renderAll()
      canvas.on('mouse:up', function (e) { getFrame(); mousePressed = false })
      canvas.on('mouse:down', function (e) { mousePressed = true })
      canvas.on('mouse:move', function (e) { recordCoor(e) })
    },
    loadSymbols () {
      this.$http.get('http://localhost:8081/static/models/class_names.txt')
        .then(response => {
          var list = response.data.split(/\n/)
          symbols = []
          for (var i = 0; i < list.length - 1; i++) {
            symbols.push(list[i])
          }
        })
        .catch(err => {
          console.log(err)
        })
    },


  }
}



function recordCoor (event) {
  // 记录当前画点的坐标
  var pointer = canvas.getPointer(event.e)
  var x = pointer.x
  var y = pointer.y

  if (x >= 0 && y >= 0 && mousePressed) {
    coords.push(pointer)
  }
}

function getMinBox () {
  var coorX = coords.map(function (p) { return p.x })
  var coorY = coords.map(function (p) { return p.y })

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
}

function getSymbols (indices) {
  var result = []
  for (var i = 0; i < indices.length; i++) {
    result[i] = symbols[indices[i]]
    return result
  }
}

function findIndicesOfMax (pred, num) {
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
}

function findTopValues (pred, num) {
  // 找到前num个预测
  var result = []
  var indices = findIndicesOfMax(pred, num)
  for (var i = 0; i < num; i++) {
    result.push(pred[indices[i]])
  }
  return result
}

// 预处理数据
function preprocess (imgData) {
  return tf.tidy(() => {
    // 转换为张量
    let tensor = tf.browser.fromPixels(imgData, 1)
    // resize
    const resized = tf.image.resizeBilinear(tensor, [28, 28]).toFloat()
    // 归一化
    const offset = tf.scalar(255.0)
    const normalized = tf.scalar(1.0).sub(resized.div(offset));

    // 增加一维
    const batched = normalized.expandDims(0)
    return batched
  })
}


function getFrame () {
  // 获取canvas的当前帧，保证至少有两个坐标点
  if (coords.length >= 2) {
    // 先得到最小的图像边框区域
    const mbb = getMinBox()
    const dpi = window.devicePixelRatio
    const imgData = canvas.contextContainer.getImageData(mbb.min.x * dpi, mbb.min.y * dpi, (mbb.max.x - mbb.min.x) * dpi, (mbb.max.y - mbb.min.y) * dpi)
    // 进行预测
    const pred = model.predict(preprocess(imgData)).dataSync()
    // 找到5个最高预测值
    const indices = findIndicesOfMax(pred, 5)
    const probs = findTopValues(pred, 5)
    const symbols = getSymbols(indices)
    // 输出结果
    console.log(symbols)
  }
}

function allowDrawing () {
  // 允许在canvas上绘图
  canvas.isDrawingMode = 1
}

// 清空画布
function erase () {
  canvas.clear();
  canvas.backgroundColor = '#ffffff';
  coords = [];
}
</script>

<style scoped>
#drawBoard {
  border: 1px solid #d1c2d3;
  position: absolute;
  top: 500px;
  left: 500px;
}
</style>
