import Product from "../../../apis/Product"

const getProduct = ({ commit }, productId) => {
    Product.show(productId)
        .then(response => {
            commit("SET_PRODUCT", response.data)
        })
}

const getProducts = ({ commit }) => {
    Product.all()
        .then(response => {
            commit("SET_PRODUCTS", response.data)
        })
}


export default {
    getProducts,
    getProduct,
}