<template>
  <div>
    <canvas id="drawBoard" width="300" height="400"></canvas>
  </div>
</template>

<script>
export default {
  name: 'QuickDraw',
  data () {
    return {
      model: null,
      canvas: null, // 还不知道是啥
      symbols: [{}],
      coords: [],
      mousePressed: false
    }
  },
  created () {
    this.loadModel()
  },
  mounted () {
    var canvas = new fabric.Canvas('drawBoard');
    canvas.backgroundColor = '#ffffff';
    canvas.isDrawingMode = 0;
    canvas.freeDrawingBrush.Color = "black";
    canvas.freeDrawingBrush.width = 10;
    canvas.renderAll();
    canvas.on('mouse:up', function (e) { getFrame(); mousePressed = false });
    canvas.on('mouse:down', function (e) { mousePressed = true });
    canvas.on('mouse:move', function (e) { recordCoor(e) })
  },
  methods: {
    async  loadModel () {
      this.model = await tf.loadModel('../../../AIModels/models/model.json')
      model.predict(tf.zeros([1, 28, 28, 1]))
      allowDrawing()
      await loadDict()
    },
    allowDrawing () {
      // 允许在canvas上绘图

    }
  }
}
</script>
