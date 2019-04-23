import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import StoryDetail from '@/components/StoryDetail'
import InformationDetail from '@/components/InformationDetail'
Vue.use(Router)

export default new Router({
  // mode: 'history',
  routes: [{
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  }, {
    path: '/story/:id',
    name: 'StoryDetail',
    component: StoryDetail
  }, {
    path: '/information/:id',
    name: 'InformationDetail',
    component: InformationDetail
  }]
})
