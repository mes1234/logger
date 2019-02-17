import Vue from 'vue'
import Router from 'vue-router'
import Login from '../components/Login'
import Logger from '../components/Logger'
import store from '../store/store'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/logger',
      name: 'logger',
      component: Logger,
      beforeEnter: (to, from, next) => {
        if (!store.state.token) {
          next('/')
        } else {
          next()
        }
      }
    }
  ]
})
