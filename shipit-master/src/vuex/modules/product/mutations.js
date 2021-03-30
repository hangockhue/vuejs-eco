const SET_PRODUCTS = (state, products) => {
    state.products = products;
}

const SET_PRODUCT = (state, product) => {
    state.product = product;
}

export default {
    SET_PRODUCTS,
    SET_PRODUCT,
}