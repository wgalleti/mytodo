axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'

window.API = {
  list_tarefas: function (params) {
    return axios.get('/api_drf/tarefas/', {params: params})
  },
  add_tarefa: function (tarefa) {
    return axios.post(`/api_drf/tarefas/`, tarefa)
  },
  finalizar_tarefa: function (tarefa) {
    return axios.post(`/api_drf/tarefas/${tarefa.id}/finalizar/`, tarefa)
  },
  remove_tarefa: function (id) {
    return axios.delete(`/api_drf/tarefas/${id}/`)
  }
}