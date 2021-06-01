
const addProductToCart = ({ commit }, {product, quantity}) => {
    commit('ADD_TO_CART', {product, quantity});
}

const removeProductFromCart = ({ commit }, product) => {
    commit('REMOVE_PRODUCT_FROM_CART', product)
}


const addOrderToServer = ( {commit}, order ) => {
    commit("REMOVE_ALL_PRODUCT")

}




export default {
    addProductToCart,
    removeProductFromCart,
    addOrderToServer
}