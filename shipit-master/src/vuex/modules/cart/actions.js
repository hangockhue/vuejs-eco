import axios from 'axios';

const addProductToCart = ({ commit }, {product, quantity}) => {
    commit('ADD_TO_CART', {product, quantity});
}

const removeProductFromCart = ({ commit }, product) => {
    commit('REMOVE_PRODUCT_FROM_CART', product)
}


const addOrderToServer = ( {commit}, {dataPost, access_token}, order ) => {
    const config = {
        headers: {
            'Content-Type': 'application/json',
            'Authorization' : 'Bearer ' + access_token
        }
    }
    axios.post('http://localhost:8000/api/order/', dataPost, config)
        .then(response => {
            commit("REMOVE_ALL_PRODUCT")
            console.log("Post thanh cong");
        })
        .catch(error => {
            commit('ERROR', error);
            console.log("Post that bai");
        })

}



export default {
    addProductToCart,
    removeProductFromCart,
    addOrderToServer
}
