import Categorys from "../../../apis/Categorys"


const getCategorys = ({ commit }) => {
    Categorys.all()
        .then(response => {
            commit('SET_CATEGORYS', response.data);
        })
}

export default {
    getCategorys
}