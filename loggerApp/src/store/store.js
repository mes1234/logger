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
    userId: false,
    projectSelectedId: 0,
    projects: ''
  },
  getters: {
    ListProjects: (state) => {
      // return all projects
      return state.projects
    },
    GetCurrentProject: (state) => {
      // return current project id
      return state.projectSelectedId
    }
  },
  mutations: {
    setCurrentProjectId: (state, projectSelected) => {
      state.projectSelectedId = projectSelected['projectSelected']
    },
    getListOfProjects: (state) => {
      axios
        .get(`http://${API}/projects`)
        .then(respons => {
          state.projects = respons.data
        })
    },
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
    },
    setCurrentProjectId: (context, payload) => {
      context.commit('setCurrentProjectId', payload)
    },
    getListOfProjects: (context, payload) => {
      context.commit('getListOfProjects', payload)
    }
  }

})
