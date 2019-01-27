import Vue from 'vue'
import Vuex from 'vuex'
import moment from 'moment'
import axios from 'axios'
import _ from 'lodash'
import router from '../router/router'
const API = '127.0.0.1:5000'
// '127.0.0.1:8081'
// 'witkepcz.pythonanywhere.com'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: false,
    username: false,
    userId: false
  },
  mutations: {
    tryLogin: (state, cred) => {
      var credToSend =
      {
        username: cred[0],
        password: cred[1]
      }
      axios
        .post(`http://${API}/login`, credToSend)
        .then(respons => {
          state.token = respons.data.access_token
          state.userId = respons.data.user_id
          axios.defaults.headers.common['Authorization'] = 'Bearer ' + state.token
          state.username = cred[0]
          router.push('/logger')
        })
        .catch(error => {
          console.log(error.response)
        })
    },
    logoutUser: (state) => {
      axios
        .get(`http://${API}/logout`)
        .then(respons => {
          state.token = false
          router.push('/')
        })
        .catch(error => {
          console.log(error.response)
        })
    }
  },
  actions: {
    tryLogin: (context, payload) => {
      context.commit('tryLogin', payload)
    },
    logoutUser: (context, payload) => {
      context.commit('logoutUser', payload)
    }
  }

})
