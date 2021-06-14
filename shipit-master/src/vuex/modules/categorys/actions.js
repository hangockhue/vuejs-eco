import Categorys from "../../../apis/Categorys"
import axios from 'axios'
// import Hightlight from "../../../apis/Hightlight"

const getCategorys = ({ commit }) => {
    Categorys.all()
        .then(response => {
            commit('SET_CATEGORYS', response.data);
        })
}

const getHightlight = ({ commit }) => {
  axios.get('http://localhost:8000/api/hightlight/')
        .then(response => {
            commit('SET_HIGHTLIGHT', response.data);
        })
}


export default {
    getCategorys,
    getHightlight,
}
