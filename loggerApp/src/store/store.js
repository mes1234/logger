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
    GetListProjects: (state) => {
      // return all projects
      return state.projects
    },
    GetCurrentProject: (state) => {
      // return current project id
      return state.projectSelectedId
    },
    GetCurrentDate: (state) => {
      return moment().format('YYYY-MM-DDTHH:mm')
    }

  },
  mutations: {
    setCurrentProjectId: (state, projectSelected) => {
      state.projectSelectedId = projectSelected['projectSelected']
    },
    UpdateListOfProjects: (state) => {
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
    },
    NewItemAdd: (state, NewItemData) => {
      var varToSend =
      {
        project_id: state.projectSelectedId,
        name: NewItemData[0],
        description: NewItemData[1],
        date: NewItemData[2] + ':00',
        owner_id: state.userId
      }
      console.log(varToSend)
      axios.post(`http://${API}/projects/${state.projectSelectedId}/items`, varToSend)
        .then(respons => {
          console.log(respons.response)
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
    UpdateListOfProjects: (context, payload) => {
      context.commit('UpdateListOfProjects', payload)
    },
    UpdateCurrentDate: (context, payload) => {
      context.commit('UpdateCurrentDate', payload)
    },
    NewItemAdd: (context, payload) => {
      context.commit('NewItemAdd', payload)
    }
  }

})
