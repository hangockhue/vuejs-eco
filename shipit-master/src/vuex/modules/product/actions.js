import Product from "../../../apis/Product"

const getProduct = ({ commit }, productId) => {
    Product.show(productId)
        .then(response => {
            commit("SET_PRODUCT", response.data)
        })
}

const getProducts = ({ commit }, categoryId) => {
    Product.all()
        .then(response => {
            var filterProduct = response.data.filter(product => product.category == categoryId)
            commit("SET_PRODUCTS", response.data)
        })
}


export default {
    getProducts,
    getProduct,
}