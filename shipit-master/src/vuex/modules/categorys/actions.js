import Categorys from "../../../apis/Categorys"
import Hightlight from "../../../apis/Hightlight"

const getCategorys = ({ commit }) => {
    Categorys.all()
        .then(response => {
            commit('SET_CATEGORYS', response.data);
        })
}

const getHightlight = ({ commit }) => {
    Highlight.all()
        .then(response => {
            commit('SET_HIGHTLIGHT', response.data);
        })
}


export default {
    getCategorys,
    getHightlight,
}
