<template>
  <div class="footer">
    <div class="foot_link">
      <a href="#">关于我们</a>
      <span>|</span>
      <a href="#">联系我们</a>
      <span>|</span>
      <a href="http://www.autism.org.uk">英国国家自闭症协会</a>
      <span>|</span>
      <a href="https://www.autismspeaks.org">自闭症之声</a>
    </div>
    <p>CopyRight &copy; 2019 Zhaofan Su, Tongji University</p>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  data () {
    return {

    }
  }
}
</script>

<style scoped>
.footer {
  border-top: 2px solid #8256c1;
  margin: 0 0;
}
.foot_link {
  text-align: center;
  margin-top: 30px;
}
.foot_link a,
.foot_link span {
  color: #8256c1;
  text-decoration: none;
}
.foot_link a:hover {
  color: #4204bf;
}
.foot_link span {
  padding: 0 10px;
}
.footer p {
  text-align: center;
  margin-top: 10px;
  margin-bottom: 20px;
}
</style>
