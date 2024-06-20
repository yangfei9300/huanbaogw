
import Vue from 'vue'
import VueRouter from 'vue-router'
import about from '../view/about.vue'
 
Vue.use(VueRouter)

const routes = [
	
  // {
  //   path: '/',
  //   name: 'index',
  //   component: index
  // },
  {
    path: '/',
    name: 'about',
    component: about
  }
]

const router = new VueRouter({
   mode: 'history',
  // base:"/gx/tfbazihehun",
  base:"/",
  routes
})

export default router
